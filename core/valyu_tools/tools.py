"""Valyu tools."""

import os
from typing import Optional, Type, List, Union, Literal
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from valyu import Valyu


def get_valyu_client(api_key: str = None) -> Valyu:
    """Get a Valyu client instance."""
    if not api_key:
        api_key = os.environ.get("VALYU_API_KEY", "")
    return Valyu(api_key=api_key)


class ValyuToolInput(BaseModel):
    """Input schema for Valyu deep search tool."""

    query: str = Field(..., description="The input query to be processed.")
    search_type: str = Field(
        default="all",
        description="Type of search: 'all', 'proprietary', or 'web'. Defaults to 'all'.",
    )
    max_num_results: int = Field(
        default=10,
        description="The maximum number of results to be returned (1-20). Defaults to 5.",
    )
    relevance_threshold: float = Field(
        default=0.5,
        description="The minimum relevance score required for a result to be included (0.0-1.0). Defaults to 0.5.",
    )
    max_price: float = Field(
        default=50.0,
        description="Maximum cost in dollars for this search. Defaults to 20.0.",
    )
    is_tool_call: bool = Field(
        default=True,
        description="Set to True when called by AI agents/tools (optimized for LLM consumption). Defaults to True.",
    )
    start_date: Optional[str] = Field(
        default=None,
        description="Start date for time filtering in YYYY-MM-DD format (optional).",
    )
    end_date: Optional[str] = Field(
        default=None,
        description="End date for time filtering in YYYY-MM-DD format (optional).",
    )
    included_sources: Optional[List[str]] = Field(
        default=None,
        description="List of URLs, domains, or datasets to include in search results (optional).",
    )
    excluded_sources: Optional[List[str]] = Field(
        default=None,
        description="List of URLs, domains, or datasets to exclude from search results (optional).",
    )
    response_length: Optional[Union[int, str]] = Field(
        default=None,
        description="Content length per item: int for character count, or 'short' (25k), 'medium' (50k), 'large' (100k), 'max' (full content) (optional).",
    )
    country_code: Optional[str] = Field(
        default=None,
        description="2-letter ISO country code (e.g., 'GB', 'US') to bias search results to a specific country (optional).",
    )
    fast_mode: bool = Field(
        default=False,
        description="Enable fast mode for faster but shorter results. Good for general purpose queries. Defaults to False.",
    )


class ValyuContentsToolInput(BaseModel):
    """Input schema for Valyu contents extraction tool."""

    urls: List[str] = Field(
        ...,
        description="List of URLs to extract content from (maximum 10 URLs per request).",
    )


class ValyuSearchTool(BaseTool):
    """Valyu deep search tool for searching proprietary and web sources."""

    name: str = "valyu_deep_search"
    description: str = (
        "A wrapper around the Valyu deep search API to search for relevant content from proprietary and web sources. "
        "Input is a query and search parameters. "
        "Output is a JSON object with the search results."
    )
    args_schema: Type[BaseModel] = ValyuToolInput
    valyu_api_key: Optional[str] = Field(default=None)

    def __init__(self, valyu_api_key: str = None, **kwargs):
        super().__init__(**kwargs)
        self._client = get_valyu_client(valyu_api_key or self.valyu_api_key)
    
    @property
    def client(self):
        return self._client

    def _run(
        self,
        query: str,
        search_type: str = "all",
        max_num_results: int = 5,
        relevance_threshold: float = 0.5,
        max_price: float = 20.0,
        is_tool_call: bool = True,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        included_sources: Optional[List[str]] = None,
        excluded_sources: Optional[List[str]] = None,
        response_length: Optional[Union[int, str]] = None,
        country_code: Optional[str] = None,
        fast_mode: bool = False,
    ) -> dict:
        """Perform a Valyu deep search."""
        return self.client.search(
            query=query,
            search_type=search_type,
            max_num_results=max_num_results,
            relevance_threshold=relevance_threshold,
            max_price=max_price,
            is_tool_call=is_tool_call,
            start_date=start_date,
            end_date=end_date,
            included_sources=included_sources,
            excluded_sources=excluded_sources,
            response_length=response_length,
            country_code=country_code,
            fast_mode=fast_mode,
        )


class ValyuContentsTool(BaseTool):
    """Valyu contents extraction tool for extracting clean content from web pages."""

    name: str = "valyu_contents_extract"
    description: str = (
        "A wrapper around the Valyu contents API to extract clean content from web pages. "
        "Input is a list of URLs. "
        "Output is a JSON object with the extracted content from each URL."
    )
    args_schema: Type[BaseModel] = ValyuContentsToolInput
    valyu_api_key: Optional[str] = Field(default=None)
    
    # User-configurable parameters
    summary: Optional[Union[bool, str]] = None
    extract_effort: Optional[Literal["normal", "high", "auto"]] = "normal"
    response_length: Optional[Union[int, str]] = "short"

    def __init__(self, valyu_api_key: str = None, **kwargs):
        super().__init__(**kwargs)
        self._client = get_valyu_client(valyu_api_key or self.valyu_api_key)
    
    @property
    def client(self):
        return self._client

    def _run(self, urls: List[str]) -> dict:
        """Extract content from URLs."""
        return self.client.contents(
            urls=urls,
            summary=self.summary,
            extract_effort=self.extract_effort,
            response_length=self.response_length,
        )
