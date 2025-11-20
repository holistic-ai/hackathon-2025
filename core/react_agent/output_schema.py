"""
Output schema for React Agent structured responses.

Users can customize this file to define their own output structure.
Simply modify the Pydantic model below to match your desired output format.
"""

from pydantic import BaseModel, Field
from typing import List, Optional


class AgentResponse(BaseModel):
    """
    Structured output schema for the React Agent.
    
    Customize this class to define your desired output format.
    The agent will automatically format its responses according to this schema.
    """
    
    # Main response content
    answer: str = Field(
        description="The main answer or response to the user's query"
    )
    
    # Sources used (optional)
    sources: Optional[List[str]] = Field(
        default=None,
        description="List of sources or references used to generate the answer"
    )
    
    # Confidence level (optional)
    confidence: Optional[str] = Field(
        default=None,
        description="Confidence level: 'high', 'medium', or 'low'"
    )
    
    # Key points (optional)
    key_points: Optional[List[str]] = Field(
        default=None,
        description="List of key points or takeaways from the response"
    )
    
    # Follow-up suggestions (optional)
    follow_up_questions: Optional[List[str]] = Field(
        default=None,
        description="Suggested follow-up questions the user might ask"
    )


# Alternative example schemas for different use cases:

class SearchResponse(BaseModel):
    """Example: Structured output for search queries"""
    summary: str = Field(description="Brief summary of findings")
    results: List[dict] = Field(description="List of search results")
    total_results: int = Field(description="Total number of results found")


class AnalysisResponse(BaseModel):
    """Example: Structured output for analysis tasks"""
    topic: str = Field(description="Topic being analyzed")
    analysis: str = Field(description="Detailed analysis")
    pros: List[str] = Field(description="Advantages or positive aspects")
    cons: List[str] = Field(description="Disadvantages or negative aspects")
    conclusion: str = Field(description="Final conclusion")


class ResearchResponse(BaseModel):
    """Example: Structured output for research tasks"""
    research_question: str = Field(description="The research question")
    findings: List[str] = Field(description="Key research findings")
    methodology: str = Field(description="How the research was conducted")
    recommendations: List[str] = Field(description="Recommendations based on findings")


# To use a different schema, simply change which class is exported as 'OutputSchema'
OutputSchema = AgentResponse  # Change this to use a different schema
