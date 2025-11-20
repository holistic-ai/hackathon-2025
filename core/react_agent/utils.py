"""Utility & helper functions."""

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import BaseMessage
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
import os

# Import Holistic AI Bedrock integration
try:
    from .holistic_ai_bedrock import HolisticAIBedrockChat
except ImportError:
    HolisticAIBedrockChat = None


def load_chat_model(model_name: str, context=None) -> BaseChatModel:
    """Load a chat model by name.

    Supports:
    - Holistic AI Bedrock Proxy models (e.g., 'claude-3-5-sonnet', 'llama3-2-90b')
    - Open-weight models via Ollama (e.g., 'gpt-oss', 'llama3.1:8b', 'qwen2.5:7b')
    - OpenAI GPT-5 series: 'gpt-5-nano', 'gpt-5-mini', 'gpt-5' (standard)

    Args:
        model_name (str): Model name
        context: Context object containing configuration, optional
    """
    try:
        # Use context configuration if provided, otherwise use defaults
        if context is not None:
            temperature = getattr(context, 'temperature', context.ollama_temperature if hasattr(context, 'ollama_temperature') else 0.7)
            timeout = context.ollama_timeout if hasattr(context, 'ollama_timeout') else 60
        else:
            temperature = 0.7
            timeout = 60
        
        # Check for Holistic AI Bedrock Proxy API (preferred for hackathon)
        team_id = os.getenv("HOLISTIC_AI_TEAM_ID")
        api_token = os.getenv("HOLISTIC_AI_API_TOKEN")
        
        if team_id and api_token and HolisticAIBedrockChat:
            # Map common model names to Bedrock model IDs
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
            
            # Use mapped model ID or original name if it looks like a Bedrock model ID
            bedrock_model = bedrock_model_map.get(model_name.lower(), model_name)
            if not bedrock_model.startswith('us.') and not bedrock_model.startswith('mistral.'):
                # Default to Claude Sonnet if not a recognized Bedrock model ID
                bedrock_model = 'us.anthropic.claude-3-5-sonnet-20241022-v2:0'
            
            print(f" Using Holistic AI Bedrock Proxy: {bedrock_model}")
            from pydantic import SecretStr
            return HolisticAIBedrockChat(
                team_id=team_id,
                api_token=SecretStr(api_token),
                model=bedrock_model,
                temperature=float(temperature),
                timeout=int(timeout),
            )
        
        # GPT-5 Series - Use OpenAI's official API (fallback)
        gpt5_models = ['gpt-5-nano', 'gpt-5-mini', 'gpt-5']
        if model_name in gpt5_models:
            openai_api_key = os.getenv("OPENAI_API_KEY")
            if not openai_api_key:
                raise ValueError(
                    f" GPT-5 model '{model_name}' requires OPENAI_API_KEY in .env file"
                )
            
            print(f" Using OpenAI GPT-5 series: {model_name}")
            # Use default max_tokens - GPT-5 manages reasoning + output tokens automatically
            return ChatOpenAI(
                model=model_name,
                api_key=openai_api_key,
                temperature=1.0,  # GPT-5 only supports default temperature
                timeout=int(timeout),
            )
        
        # Open-weight models via Ollama
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        
        # For models that support OpenAI-style tool calling, use ChatOpenAI with Ollama backend
        if model_name.startswith('gpt-oss') or model_name.startswith('qwen3'):
            print(f" Using ChatOpenAI backend for {model_name} (Ollama, native tool calling)")
            return ChatOpenAI(
                model=model_name,
                base_url=f"{base_url}/v1",  # Use OpenAI-compatible endpoint
                api_key="ollama",  # Dummy key for local Ollama
                temperature=float(temperature),
                timeout=int(timeout),
            )
        else:
            # For other Ollama models, use standard ChatOllama
            print(f" Using ChatOllama backend for {model_name}")
            return ChatOllama(
                model=model_name,
                base_url=base_url,
                temperature=temperature,
                timeout=timeout,
            )
            
    except Exception as e:
        if 'holistic' in str(e).lower() or 'bedrock' in str(e).lower():
            print(f" Failed to connect to Holistic AI Bedrock Proxy with model '{model_name}': {e}")
            print("Please check:")
            print("1. HOLISTIC_AI_TEAM_ID is set in .env file")
            print("2. HOLISTIC_AI_API_TOKEN is set in .env file")
            print("3. Model name is valid for Bedrock Proxy API")
        elif 'gpt-5' in model_name:
            print(f" Failed to connect to OpenAI with model '{model_name}': {e}")
            print("Please check:")
            print("1. OPENAI_API_KEY is set in .env file")
            print("2. You have access to GPT-5 series models")
        else:
            print(f" Failed to connect to Ollama with model '{model_name}': {e}")
            print("Please check:")
            print("1. Ollama is running: ollama serve")
            print(f"2. Model '{model_name}' is available: ollama list")
            print("3. API is accessible: curl http://localhost:11434/api/version")
        raise
