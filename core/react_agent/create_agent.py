"""Local implementation of create_react_agent function with structured output"""

from typing import Optional, Callable, Any, List, Type
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.base import BaseCheckpointSaver
from pydantic import BaseModel

# Import local modules
from .context import Context
from .state import InputState, State


def create_react_agent(
    tools: List[Callable[..., Any]],
    checkpointer: Optional[BaseCheckpointSaver] = None,
    context: Optional[Context] = None,
    model_name: Optional[str] = None,
    output_schema: Optional[Type[BaseModel]] = None,
    system_prompt: Optional[str] = None
):
    """Create ReAct agent with optional structured output
    
    Args:
        tools: List of tools to provide to the agent
        checkpointer: Optional checkpoint saver for conversation history.
                     Defaults to None for simplicity and performance.
                     Pass MemorySaver() or custom checkpointer if needed.
        context: Context configuration (defaults to Context())
        model_name: Model name (overrides context.model if provided)
        output_schema: Optional Pydantic schema for structured output.
                      If None (default), returns natural text responses.
                      If provided, formats responses as validated JSON.
        system_prompt: Optional custom system prompt (overrides default).
                      If provided, this will be used instead of the default prompt.
        
    Returns:
        Compiled LangGraph agent
    """
    
    # Setup context
    if context is None:
        context = Context()
    if model_name is not None:
        context.model = model_name
    if system_prompt is not None:
        context.system_prompt = system_prompt
    
    # Setup output schema (optional - only if explicitly provided)
    use_structured_output = output_schema is not None
    if use_structured_output:
        print(f" Using structured output: {output_schema.__name__}")
    
    # Load and configure model
    from .utils import load_chat_model
    model = load_chat_model(context.model, context)
    model = model.bind(stream=False)
    
    # Bind tools if provided
    if tools:
        # Holistic AI Bedrock, GPT-5 and OpenAI-compatible Ollama models support native tool calling
        gpt5_models = ['gpt-5-nano', 'gpt-5-mini', 'gpt-5']
        bedrock_models = ['claude', 'llama', 'nova', 'mistral']
        model_supports_tools = (
            context.model in gpt5_models or 
            context.model.startswith('gpt-oss') or 
            context.model.startswith('qwen3') or
            any(bedrock_model in context.model.lower() for bedrock_model in bedrock_models) or
            context.model.startswith('us.anthropic') or
            context.model.startswith('us.meta') or
            context.model.startswith('us.amazon')
        )
        if model_supports_tools:
            model = model.bind_tools(tools)
            print(" Native tool calling enabled")
        else:
            print("  Fallback tool calling mode")
    
    # Setup checkpointer (optional - defaults to None for simplicity and speed)
    # Users can pass their own checkpointer if they need conversation history
    if checkpointer is False:
        checkpointer = None  # Explicitly disabled
    
    # Build graph
    builder = StateGraph(State, input_schema=InputState, context_schema=Context)
    
    # Model calling node
    def call_model(state: State, *, runtime=None):
        """Call the model with tools."""
        from datetime import UTC, datetime
        from langchain_core.messages import AIMessage
        from typing import cast
        
        context_to_use = runtime.context if (runtime and runtime.context) else context
        
        system_message = context_to_use.system_prompt.format(
            system_time=datetime.now(tz=UTC).isoformat()
        )
        
        # Convert messages to LangChain format
        messages_to_send = []
        # Add system message if supported by model
        # For Holistic AI Bedrock, we'll include it in the messages
        from langchain_core.messages import SystemMessage
        messages_to_send.append(SystemMessage(content=system_message))
        messages_to_send.extend(state.messages)
        
        response = cast(
            AIMessage,
            model.invoke(messages_to_send),
        )
        
        if state.is_last_step and response.tool_calls:
            return {
                "messages": [
                    AIMessage(
                        id=response.id,
                        content="Sorry, could not complete in the specified steps.",
                    )
                ]
            }
        
        return {"messages": [response]}
    
    # Add nodes
    builder.add_node("call_model", call_model)
    builder.add_node("tools", ToolNode(tools))
    
    # Structured output formatting node (only if schema provided)
    def format_output(state: State, *, runtime=None):
        """Format response as structured JSON."""
        from langchain_core.messages import AIMessage, HumanMessage
        import json
        
        last_message = state.messages[-1]
        
        if isinstance(last_message, AIMessage) and not last_message.tool_calls:
            schema_fields = output_schema.model_json_schema()
            
            format_prompt = f"""Format the previous response as a valid JSON object following this schema:

{json.dumps(schema_fields, indent=2)}

IMPORTANT: Return ONLY valid JSON with no additional text, explanations, or thinking process. Start with {{ and end with }}."""
            
            format_response = model.invoke([*state.messages, HumanMessage(content=format_prompt)])
            
            try:
                # Extract JSON - robust parsing for various model outputs
                content = format_response.content.strip()
                
                # Remove markdown code blocks
                if '```json' in content:
                    content = content.split('```json')[1].split('```')[0].strip()
                elif '```' in content:
                    content = content.split('```')[1].split('```')[0].strip()
                
                # Find the first complete JSON object
                start = content.find('{')
                if start == -1:
                    raise ValueError("No JSON object found in response")
                
                # Count braces to find the matching closing brace
                brace_count = 0
                end = start
                for i in range(start, len(content)):
                    if content[i] == '{':
                        brace_count += 1
                    elif content[i] == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            end = i + 1
                            break
                
                content = content[start:end]
                
                # Parse and validate
                structured_data = json.loads(content)
                validated_data = output_schema(**structured_data)
                
                return {
                    "messages": [
                        AIMessage(
                            content=validated_data.model_dump_json(indent=2),
                            additional_kwargs={"structured_output": validated_data.model_dump()}
                        )
                    ]
                }
            except Exception as e:
                return {
                    "messages": [
                        AIMessage(content=f"Error formatting output: {e}\n\n{format_response.content}")
                    ]
                }
        
        return {"messages": []}
    
    # Only add format_output node if structured output is enabled
    if use_structured_output:
        builder.add_node("format_output", format_output)
    
    # Setup graph edges
    if use_structured_output:
        def route_output(state: State):
            """Route to tools or format_output based on model response."""
            from langchain_core.messages import AIMessage
            last_message = state.messages[-1]
            if not isinstance(last_message, AIMessage):
                raise ValueError(f"Expected AIMessage, got {type(last_message).__name__}")
            return "tools" if last_message.tool_calls else "format_output"
        
        builder.add_edge("__start__", "call_model")
        builder.add_conditional_edges("call_model", route_output, ["tools", "format_output"])
        builder.add_edge("tools", "call_model")
        builder.add_edge("format_output", "__end__")
    else:
        # Without structured output, simpler routing
        def route_simple(state: State):
            """Route to tools or end based on model response."""
            from langchain_core.messages import AIMessage
            last_message = state.messages[-1]
            if not isinstance(last_message, AIMessage):
                raise ValueError(f"Expected AIMessage, got {type(last_message).__name__}")
            return "tools" if last_message.tool_calls else "__end__"
        
        builder.add_edge("__start__", "call_model")
        builder.add_conditional_edges("call_model", route_simple, ["tools", "__end__"])
        builder.add_edge("tools", "call_model")
    
    # Compile and return
    return builder.compile(checkpointer=checkpointer, name="ReAct Agent")