"""Valyu retrievers."""

import os
from typing import List, Optional, Union, Literal
from langchain_core.callbacks import CallbackManagerForRetrieverRun
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from pydantic import Field
from valyu import Valyu


def get_valyu_client(api_key: str = None) -> Valyu:
    """Get a Valyu client instance."""
    if not api_key:
        api_key = os.environ.get("VALYU_API_KEY", "")
    return Valyu(api_key=api_key)


def _get_valyu_metadata(result) -> dict:
    """Extract metadata from Valyu search result."""
    metadata = {
        "title": getattr(result, "title", None),
        "url": getattr(result, "url", None),
        "source": getattr(result, "source", None),
        "price": getattr(result, "price", None),
        "length": getattr(result, "length", None),
        "data_type": getattr(result, "data_type", None),
        "relevance_score": getattr(result, "relevance_score", None),
    }
    if hasattr(result, "image_url") and result.image_url:
        metadata["image_url"] = result.image_url
    return metadata


def _get_contents_metadata(result) -> dict:
    """Extract metadata from Valyu contents result."""
    metadata = {
        "url": getattr(result, "url", None),
        "title": getattr(result, "title", None),
        "status": getattr(result, "status", None),
        "price": getattr(result, "price", None),
        "length": getattr(result, "length", None),
        "extraction_effort": getattr(result, "extraction_effort", None),
    }
    if hasattr(result, "error") and result.error:
        metadata["error"] = result.error
    return metadata


class ValyuRetriever(BaseRetriever):
    """Retriever for Valyu deep search API."""

    k: int = 10
    search_type: str = "all"
    relevance_threshold: float = 0.5
    max_price: float = 50.0
    is_tool_call: bool = True
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    included_sources: Optional[List[str]] = None
    excluded_sources: Optional[List[str]] = None
    response_length: Optional[Union[int, str]] = None
    country_code: Optional[str] = None
    fast_mode: bool = False
    valyu_api_key: Optional[str] = Field(default=None)

    def __init__(self, valyu_api_key: str = None, **kwargs):
        super().__init__(**kwargs)
        self._client = get_valyu_client(valyu_api_key or self.valyu_api_key)
    
    @property
    def client(self):
        return self._client

    def _get_relevant_documents(
        self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        """Get relevant documents from Valyu search."""
        response = self.client.search(
            query=query,
            search_type=self.search_type,
            max_num_results=self.k,
            relevance_threshold=self.relevance_threshold,
            max_price=self.max_price,
            is_tool_call=self.is_tool_call,
            start_date=self.start_date,
            end_date=self.end_date,
            included_sources=self.included_sources,
            excluded_sources=self.excluded_sources,
            response_length=self.response_length,
            country_code=self.country_code,
            fast_mode=self.fast_mode,
        )
        
        results = getattr(response, "results", [])
        return [
            Document(
                page_content=str(getattr(result, "content", "")),
                metadata=_get_valyu_metadata(result),
            )
            for result in results
        ]


class ValyuContentsRetriever(BaseRetriever):
    """Retriever for Valyu contents extraction API."""

    urls: List[str] = Field(default_factory=list)
    summary: Optional[Union[bool, str]] = None
    extract_effort: Optional[Literal["normal", "high", "auto"]] = "normal"
    response_length: Optional[Union[int, str]] = "short"
    valyu_api_key: Optional[str] = Field(default=None)

    def __init__(self, valyu_api_key: str = None, **kwargs):
        super().__init__(**kwargs)
        self._client = get_valyu_client(valyu_api_key or self.valyu_api_key)
    
    @property
    def client(self):
        return self._client

    def _get_relevant_documents(
        self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        """Get documents by extracting content from URLs."""
        # Use pre-configured URLs or parse from query
        urls = self.urls if self.urls else [url.strip() for url in query.split(",") if url.strip()]
        
        if not urls:
            return []

        response = self.client.contents(
            urls=urls,
            summary=self.summary,
            extract_effort=self.extract_effort,
            response_length=self.response_length,
        )

        results = getattr(response, "results", [])
        return [
            Document(
                page_content=str(getattr(result, "content", "")),
                metadata=_get_contents_metadata(result),
            )
            for result in results
        ]
