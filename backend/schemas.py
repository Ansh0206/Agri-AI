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


class WeatherRiskRequest(BaseModel):
    crop: str = Field(default="Tomato", min_length=2, max_length=50)
    district: str = Field(default="Nashik", min_length=2, max_length=80)


class WeatherRiskResponse(BaseModel):
    crop: str
    district: str
    temperature_c: int
    humidity_percent: int
    rain_chance_percent: int
    wind_kmph: int
    risk_level: Literal["low", "medium", "high"]
    disease_pressure: str
    advice: str
    next_24_hours: list[str]


class MarketPriceRequest(BaseModel):
    crop: str = Field(default="Tomato", min_length=2, max_length=50)
    district: str = Field(default="Nashik", min_length=2, max_length=80)


class PricePoint(BaseModel):
    label: str
    price: int


class MarketPriceResponse(BaseModel):
    crop: str
    district: str
    mandi: str
    today_price: int
    yesterday_price: int
    unit: str
    trend: Literal["rising", "stable", "falling"]
    change_percent: float
    advice: str
    price_history: list[PricePoint]


class LocalAdviceRequest(BaseModel):
    crop: str = Field(default="Tomato", min_length=2, max_length=50)
    district: str = Field(default="Nashik", min_length=2, max_length=80)
    language: Literal["English", "Hindi"] = "English"
    question: str = Field(default="", max_length=500)


class LocalAdviceResponse(BaseModel):
    crop: str
    district: str
    language: Literal["English", "Hindi"]
    answer: str
    key_points: list[str]
    confidence: float
