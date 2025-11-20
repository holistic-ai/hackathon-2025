"""Holistic AI Bedrock Proxy API wrapper for tutorials.

This is a self-contained wrapper that can be used in tutorials without importing from ../core.
"""

import os
import json
import requests
from typing import List, Optional, Any, Iterator, Type
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage, SystemMessage
from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.outputs import ChatGeneration, ChatResult
from pydantic import Field, SecretStr, BaseModel as PydanticBaseModel


class HolisticAIBedrockChat(BaseChatModel):
    """Chat model for Holistic AI Bedrock Proxy API (for tutorials)."""
    
    api_endpoint: str = Field(
        default="https://ctwa92wg1b.execute-api.us-east-1.amazonaws.com/prod/invoke",
        description="API endpoint URL"
    )
    
    team_id: str = Field(description="Team ID for authentication")
    api_token: SecretStr = Field(description="API token for authentication")
    
    model: str = Field(
        default="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
        description="Model identifier"
    )
    
    max_tokens: int = Field(default=1024, description="Maximum tokens to generate")
    temperature: float = Field(default=0.7, description="Temperature for generation")
    timeout: int = Field(default=60, description="Request timeout in seconds")
    
    class Config:
        arbitrary_types_allowed = True
    
    @property
    def _llm_type(self) -> str:
        return "holistic_ai_bedrock"
    
    def _convert_messages_to_api_format(self, messages: List[BaseMessage]) -> List[dict]:
        """Convert LangChain messages to API format."""
        from langchain_core.messages import ToolMessage
        
        api_messages = []
        for msg in messages:
            if isinstance(msg, SystemMessage):
                continue
            elif isinstance(msg, HumanMessage):
                api_messages.append({"role": "user", "content": msg.content})
            elif isinstance(msg, AIMessage):
                # Handle AIMessage - include content and tool_calls if present
                if hasattr(msg, 'tool_calls') and msg.tool_calls:
                    # Convert tool_calls to Claude format (content blocks)
                    content_blocks = []
                    if msg.content:
                        content_blocks.append({"type": "text", "text": msg.content})
                    for tc in msg.tool_calls:
                        tc_name = tc.get('name') if isinstance(tc, dict) else getattr(tc, 'name', '')
                        tc_args = tc.get('args') if isinstance(tc, dict) else getattr(tc, 'args', {})
                        tc_id = tc.get('id') if isinstance(tc, dict) else getattr(tc, 'id', '')
                        content_blocks.append({
                            "type": "tool_use",
                            "id": tc_id,
                            "name": tc_name,
                            "input": tc_args
                        })
                    api_messages.append({"role": "assistant", "content": content_blocks})
                else:
                    api_messages.append({"role": "assistant", "content": msg.content})
            elif isinstance(msg, ToolMessage):
                # Handle ToolMessage - convert to Claude tool_result format
                tool_call_id = msg.tool_call_id if hasattr(msg, 'tool_call_id') else ""
                tool_result_content = [{
                    "type": "tool_result",
                    "tool_use_id": tool_call_id,
                    "content": str(msg.content)
                }]
                api_messages.append({"role": "user", "content": tool_result_content})
            else:
                api_messages.append({"role": "user", "content": str(msg.content)})
        return api_messages
    
    def _extract_system_prompt(self, messages: List[BaseMessage]) -> Optional[str]:
        """Extract system prompt from messages."""
        for msg in messages:
            if isinstance(msg, SystemMessage):
                return msg.content
        return None
    
    def bind_tools(self, tools: List[Any], **kwargs: Any) -> "HolisticAIBedrockChat":
        """Bind tools to the model for tool calling."""
        bound_model = self.__class__(
            api_endpoint=self.api_endpoint,
            team_id=self.team_id,
            api_token=self.api_token,
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            timeout=self.timeout,
        )
        bound_model._bound_tools = tools
        return bound_model
    
    def with_structured_output(
        self,
        schema: Type[PydanticBaseModel],
        **kwargs: Any,
    ) -> "HolisticAIBedrockStructuredOutput":
        """Create a model that returns structured output matching the schema.
        
        Uses Holistic AI Bedrock API's response_format feature for native structured output.
        """
        return HolisticAIBedrockStructuredOutput(
            base_model=self,
            schema=schema,
            **kwargs
        )
    
    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:
        """Generate chat response."""
        tools = kwargs.get("tools") or getattr(self, "_bound_tools", None)
        
        system_prompt = self._extract_system_prompt(messages)
        api_messages = self._convert_messages_to_api_format(messages)
        
        if system_prompt:
            api_messages.insert(0, {"role": "user", "content": f"System: {system_prompt}"})
        
        payload = {
            "team_id": self.team_id,
            "api_token": self.api_token.get_secret_value(),
            "model": self.model,
            "messages": api_messages,
            "max_tokens": self.max_tokens,
        }
        
        if self.temperature is not None:
            payload["temperature"] = self.temperature
        
        # Check for response_format (for structured output)
        response_format = kwargs.get("response_format") or getattr(self, "_response_format", None)
        if response_format:
            payload["response_format"] = response_format
            # When using response_format, we should NOT include tools in the same request
            # The API may not support both simultaneously
            # Tools should be handled separately before structured output
            tools = None  # Disable tools when using response_format
        
        if tools:
            # Check if tools is actually a list of tool objects
            # (with_structured_output might pass schema objects or other non-tool objects)
            tools_list = []
            for tool in tools:
                # Only process if it's a tool object with 'name' and 'description' attributes
                # Skip Pydantic schemas and other non-tool objects
                if (hasattr(tool, 'name') and 
                    hasattr(tool, 'description') and 
                    callable(getattr(tool, 'name', None)) == False):  # name should not be callable
                    try:
                        tool_dict = {
                            "name": tool.name,
                            "description": tool.description,
                            "input_schema": tool.args_schema.model_json_schema() if hasattr(tool, "args_schema") else {}
                        }
                        tools_list.append(tool_dict)
                    except Exception:
                        # Skip if we can't process this tool
                        continue
            
            if tools_list:
                payload["tools"] = tools_list
                payload["tool_choice"] = {"type": "auto"}
        
        headers = {
            "Content-Type": "application/json",
            "X-Team-ID": self.team_id,
            "X-API-Token": self.api_token.get_secret_value(),
        }
        
        try:
            response = requests.post(
                self.api_endpoint,
                headers=headers,
                json=payload,
                timeout=self.timeout,
            )
            response.raise_for_status()
            
            result = response.json()
            
            content = ""
            tool_calls = []
            
            # Handle structured output response format
            # According to API docs, structured JSON is in result["content"][0]["text"]
            if response_format and "content" in result and len(result["content"]) > 0:
                # For structured output, content is a JSON string in result["content"][0]["text"]
                first_block = result["content"][0]
                if isinstance(first_block, dict):
                    if first_block.get("type") == "text":
                        content = first_block.get("text", "")
                    else:
                        # Fallback: try to get text from any field
                        content = first_block.get("text", str(first_block))
                else:
                    content = str(first_block)
            elif "content" in result and len(result["content"]) > 0:
                # Regular response format
                for content_block in result["content"]:
                    if isinstance(content_block, dict):
                        if content_block.get("type") == "text":
                            text = content_block.get("text", "")
                            if text:
                                content += text + "\n" if content else text
                        elif content_block.get("type") == "tool_use":
                            tool_calls.append({
                                "name": content_block.get("name", ""),
                                "args": content_block.get("input", {}),
                                "id": content_block.get("id", "")
                            })
                    elif isinstance(content_block, str):
                        content += content_block
                
                content = content.rstrip("\n")
            elif "text" in result:
                content = result["text"]
            else:
                content = str(result)
            
            # Create AIMessage - use dict format for tool_calls
            # Reference: langchain-aws ChatBedrockConverse uses dict format
            # LangChain automatically handles dict format for tool_calls
            # If response_format was used, content is JSON string that needs parsing
            if response_format and content:
                # Content is JSON string from structured output
                # Store raw JSON in message content
                message = AIMessage(content=content)
            elif tool_calls:
                # When there are tool calls, use dict format directly
                # LangChain's AIMessage constructor accepts dict format
                message = AIMessage(content="", tool_calls=tool_calls)
            else:
                message = AIMessage(content=content)
            
            generation = ChatGeneration(message=message)
            return ChatResult(generations=[generation])
            
        except requests.exceptions.RequestException as e:
            error_msg = f"Error calling Holistic AI Bedrock API: {e}"
            if hasattr(e, 'response') and e.response:
                try:
                    error_detail = e.response.text
                    error_msg += f"\nResponse: {error_detail}"
                    # Try to parse JSON error if available
                    try:
                        error_json = e.response.json()
                        error_msg += f"\nError details: {json.dumps(error_json, indent=2)}"
                    except:
                        pass
                except:
                    pass
            raise ValueError(error_msg)
    
    def _stream(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> Iterator[ChatGeneration]:
        """Stream chat response."""
        result = self._generate(messages, stop=stop, run_manager=run_manager, **kwargs)
        yield result.generations[0]


class HolisticAIBedrockStructuredOutput:
    """Wrapper for structured output using Holistic AI Bedrock API's response_format."""
    
    def __init__(
        self,
        base_model: HolisticAIBedrockChat,
        schema: Type[PydanticBaseModel],
        **kwargs: Any,
    ):
        self.base_model = base_model
        self.schema = schema
        
        # Get JSON schema from Pydantic model
        json_schema = schema.model_json_schema()
        
        # According to API docs, we can pass Pydantic's JSON schema directly
        # The API will automatically wrap it in the correct format
        # But we still need to clean it up to remove Pydantic-specific fields
        cleaned_schema = {
            "type": json_schema.get("type", "object"),
            "properties": {},
            "required": json_schema.get("required", []),
        }
        
        # Clean up properties - remove Pydantic-specific fields like "title"
        for key, value in json_schema.get("properties", {}).items():
            cleaned_prop = {}
            if "type" in value:
                cleaned_prop["type"] = value["type"]
            if "description" in value:
                cleaned_prop["description"] = value["description"]
            if "items" in value:
                # Clean items as well - remove "title" and other non-standard fields
                cleaned_items = {}
                if "type" in value["items"]:
                    cleaned_items["type"] = value["items"]["type"]
                cleaned_prop["items"] = cleaned_items
            if "enum" in value:
                cleaned_prop["enum"] = value["enum"]
            # Handle constraints
            if "minimum" in value:
                cleaned_prop["minimum"] = value["minimum"]
            if "maximum" in value:
                cleaned_prop["maximum"] = value["maximum"]
            cleaned_schema["properties"][key] = cleaned_prop
        
        # Create response_format for API
        # According to docs, we can pass the schema directly
        self._response_format = {
            "type": "json_schema",
            "json_schema": {
                "name": schema.__name__.lower(),
                "strict": True,
                "schema": cleaned_schema
            }
        }
    
    def invoke(self, input: Any, config: Optional[Any] = None, **kwargs: Any) -> PydanticBaseModel:
        """Invoke the model and return structured output."""
        from langchain_core.messages import ToolMessage
        
        # Convert input to messages if needed
        if isinstance(input, str):
            messages = [HumanMessage(content=input)]
        elif isinstance(input, list):
            messages = input
        elif hasattr(input, "messages"):
            messages = input.messages
        else:
            messages = [HumanMessage(content=str(input))]
        
        # When using structured output with agents, the messages may contain tool call history
        # For structured output, we need to extract just the final AI response content
        # and use it as a simple prompt for structured output
        messages_to_use = []
        last_ai_content = None
        
        # Find the last AI message without tool calls (final response)
        for msg in reversed(messages):
            if isinstance(msg, AIMessage) and not (hasattr(msg, 'tool_calls') and msg.tool_calls):
                if msg.content:
                    last_ai_content = msg.content
                    break
        
        # If we found a final AI response, use its content as the prompt
        # Otherwise, use the original messages
        if last_ai_content:
            # Use the final AI response content as input for structured output
            messages_to_use = [HumanMessage(content=f"Format the following information as structured JSON:\n\n{last_ai_content}")]
        else:
            # Fallback: use original messages
            messages_to_use = messages
        
        # Call _generate with response_format
        try:
            result = self.base_model._generate(
                messages=messages_to_use,
                response_format=self._response_format,
                **kwargs
            )
        except ValueError as e:
            # If API returns error, provide helpful message
            error_str = str(e)
            if "500" in error_str or "Internal Server Error" in error_str:
                raise ValueError(
                    f"Holistic AI Bedrock API returned an error with structured output.\n"
                    f"This may occur when:\n"
                    f"1. Combining tools and structured output\n"
                    f"2. API temporarily unavailable\n"
                    f"3. response_format feature limitations\n\n"
                    f"Original error: {error_str}\n\n"
                    f"💡 Solution: Use OpenAI for agent + structured output:\n"
                    f"  from langchain_openai import ChatOpenAI\n"
                    f"  llm_openai = ChatOpenAI(model='gpt-5-mini')\n"
                    f"  agent = create_react_agent(llm_openai, tools=[...], response_format={self.schema.__name__})"
                )
            raise
        
        # Extract JSON from response
        content = result.generations[0].message.content
        
        # Parse JSON and validate with Pydantic
        try:
            if isinstance(content, str):
                json_data = json.loads(content)
            else:
                json_data = content
            
            # Validate and return Pydantic object
            return self.schema.model_validate(json_data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON from structured output: {e}\nContent: {content}")
        except Exception as e:
            raise ValueError(f"Failed to validate structured output: {e}\nContent: {content}")
    
    def __call__(self, input: Any, **kwargs: Any) -> PydanticBaseModel:
        """Make the wrapper callable."""
        return self.invoke(input, **kwargs)


def get_chat_model(model_name: str = "claude-3-5-sonnet", use_openai: bool = False, **kwargs):
    """Get a chat model - uses Holistic AI Bedrock by default.
    
    Args:
        model_name: Model name. Can be:
            - Short names: 'claude-3-5-sonnet', 'claude-3-5-haiku', 'llama3-2-90b', etc.
            - Full Bedrock IDs: 'us.anthropic.claude-3-5-sonnet-20241022-v2:0'
            - OpenAI models: 'gpt-5-nano', 'gpt-5-mini', 'gpt-5' (only if use_openai=True)
        use_openai: If True, use OpenAI instead of Bedrock (optional alternative)
        **kwargs: Additional arguments for the model
    
    Returns:
        ChatModel instance
    
    Raises:
        ValueError: If Bedrock credentials not set and use_openai=False
    """
    from langchain_openai import ChatOpenAI
    
    # Model name mapping
    bedrock_model_map = {
        'claude-3-5-sonnet': 'us.anthropic.claude-3-5-sonnet-20241022-v2:0',
        'claude-3-5-haiku': 'us.anthropic.claude-3-5-haiku-20241022-v1:0',
        'claude-3-opus': 'us.anthropic.claude-3-opus-20240229-v1:0',
        'claude-3-sonnet': 'us.anthropic.claude-3-sonnet-20240229-v1:0',
        'claude-3-haiku': 'us.anthropic.claude-3-haiku-20240307-v1:0',
        'llama3-2-90b': 'us.meta.llama3-2-90b-instruct-v1:0',
        'llama3-2-11b': 'us.meta.llama3-2-11b-instruct-v1:0',
        'llama3-2-3b': 'us.meta.llama3-2-3b-instruct-v1:0',
        'nova-pro': 'us.amazon.nova-pro-v1:0',
        'nova-lite': 'us.amazon.nova-lite-v1:0',
    }
    
    # Check for Holistic AI Bedrock credentials
    team_id = os.getenv("HOLISTIC_AI_TEAM_ID")
    api_token = os.getenv("HOLISTIC_AI_API_TOKEN")
    
    # If explicitly requesting OpenAI, use it
    if use_openai:
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError(
                "OPENAI_API_KEY not set. To use OpenAI, set OPENAI_API_KEY in your .env file.\n"
                "Alternatively, use Holistic AI Bedrock by setting HOLISTIC_AI_TEAM_ID and HOLISTIC_AI_API_TOKEN."
            )
        print("ℹ️  Using OpenAI (optional alternative)")
        return ChatOpenAI(model=model_name, **kwargs)
    
    # GPT model names require explicit use_openai=True
    if model_name in ['gpt-5-nano', 'gpt-5-mini', 'gpt-5']:
        raise ValueError(
            f"Model '{model_name}' requires OpenAI. To use OpenAI, call get_chat_model('{model_name}', use_openai=True) and set OPENAI_API_KEY.\n"
            "Alternatively, use Holistic AI Bedrock models (e.g., 'claude-3-5-sonnet') by setting HOLISTIC_AI_TEAM_ID and HOLISTIC_AI_API_TOKEN."
        )
    
    # Use Holistic AI Bedrock (recommended/default)
    if not team_id or not api_token:
        raise ValueError(
            "HOLISTIC_AI_TEAM_ID and HOLISTIC_AI_API_TOKEN not set.\n"
            "Please set these in your .env file to use Holistic AI Bedrock (recommended).\n"
            "Alternatively, use OpenAI by calling get_chat_model(model_name, use_openai=True)"
        )
    
    bedrock_model = bedrock_model_map.get(model_name.lower(), model_name)
    if not bedrock_model.startswith('us.') and not bedrock_model.startswith('mistral.'):
        bedrock_model = 'us.anthropic.claude-3-5-sonnet-20241022-v2:0'
    
    from pydantic import SecretStr
    return HolisticAIBedrockChat(
        team_id=team_id,
        api_token=SecretStr(api_token),
        model=bedrock_model,
        temperature=kwargs.get('temperature', 0.7),
        max_tokens=kwargs.get('max_tokens', 1024),
        timeout=kwargs.get('timeout', 60),
    )

