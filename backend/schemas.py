from typing import Literal

from pydantic import BaseModel, Field


class AdvisoryRequest(BaseModel):
    crop: str = Field(default="Tomato", min_length=2, max_length=50)
    district: str = Field(default="Nashik", min_length=2, max_length=80)
    language: str = Field(default="English", min_length=2, max_length=40)
    question: str = Field(default="", max_length=500)


class Recommendation(BaseModel):
    title: str
    detail: str
    priority: Literal["low", "medium", "high"]


class AgentResult(BaseModel):
    agent: str
    status: Literal["ready", "mocked", "planned"]
    summary: str
    confidence: float


class AdvisoryResponse(BaseModel):
    crop: str
    district: str
    language: str
    summary: str
    overall_confidence: float
    recommendations: list[Recommendation]
    agent_results: list[AgentResult]


class DiseaseAnalysisResponse(BaseModel):
    crop: str
    filename: str
    disease: str
    confidence: float
    severity: Literal["low", "medium", "high"]
    symptoms: list[str]
    treatment: list[str]
    prevention: list[str]
    note: str
