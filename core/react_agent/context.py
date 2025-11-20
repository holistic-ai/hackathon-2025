"""Define the configurable parameters for the agent."""

from __future__ import annotations

import os
from dataclasses import dataclass, field, fields
from typing import Annotated

from . import prompts


@dataclass(kw_only=True)
class Context:
    """The context for the agent."""

    system_prompt: str = field(
        default=prompts.EXPERIMENT_SYSTEM_PROMPT,
        metadata={
            "description": "The system prompt to use for the agent's interactions. "
            "This prompt sets the context and behavior for the agent."
        },
    )

    model: Annotated[str, {"__template_metadata__": {"kind": "llm"}}] = field(
        default="claude-3-5-sonnet",
        metadata={
            "description": "The model to use. Defaults to 'claude-3-5-sonnet' (Holistic AI Bedrock). "
            "Can be a Bedrock model ID (e.g., 'us.anthropic.claude-3-5-sonnet-20241022-v2:0') "
            "or a short name (e.g., 'claude-3-5-sonnet', 'llama3-2-90b')."
        },
    )

    max_search_results: int = field(
        default=10,
        metadata={
            "description": "The maximum number of search results to return for each search query."
        },
    )
    
    # Ollama 
    ollama_temperature: float = field(
        default=0.1,
        metadata={
            "description": "Temperature for Ollama model (0.0 to 1.0)"
        },
    )
    
    ollama_timeout: int = field(
        default=60,
        metadata={
            "description": "Timeout for Ollama requests in seconds"
        },
    )
    
    ollama_num_predict: int = field(
        default=256,
        metadata={
            "description": "Maximum number of tokens to predict"
        },
    )

    def __post_init__(self) -> None:
        """Fetch env vars for attributes that were not passed as args."""
        for f in fields(self):
            if not f.init:
                continue

            if getattr(self, f.name) == f.default:
                setattr(self, f.name, os.environ.get(f.name.upper(), f.default))
