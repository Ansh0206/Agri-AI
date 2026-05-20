from typing import Literal

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


app = FastAPI(
    title="Agri-AI Backend",
    description="Software-only multi-agent backend for agricultural decision-making.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


AGENTS = [
    {
        "id": "disease",
        "name": "Disease Agent",
        "phase": "MVP",
        "status": "mocked",
        "description": "Analyzes crop images and symptoms to suggest likely disease risk.",
    },
    {
        "id": "weather",
        "name": "Weather Agent",
        "phase": "MVP",
        "status": "mocked",
        "description": "Converts weather forecast signals into farm-risk alerts.",
    },
    {
        "id": "market",
        "name": "Market Agent",
        "phase": "MVP",
        "status": "mocked",
        "description": "Explains mandi price trends and selling-window guidance.",
    },
    {
        "id": "voice",
        "name": "Voice Agent",
        "phase": "MVP",
        "status": "planned",
        "description": "Handles local-language farmer questions through text and voice.",
    },
    {
        "id": "scheme",
        "name": "Scheme Agent",
        "phase": "Phase 2",
        "status": "planned",
        "description": "Retrieves government scheme eligibility and required documents.",
    },
    {
        "id": "pest",
        "name": "Pest Agent",
        "phase": "Phase 2",
        "status": "planned",
        "description": "Predicts pest risk from crop, season, region, and weather.",
    },
]


@app.get("/")
def root() -> dict[str, str]:
    return {
        "name": "Agri-AI Backend",
        "message": "FastAPI backend is running.",
        "docs": "/docs",
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/agents")
def list_agents() -> dict[str, list[dict[str, str]]]:
    return {"agents": AGENTS}


@app.post("/advisory", response_model=AdvisoryResponse)
def create_advisory(request: AdvisoryRequest) -> AdvisoryResponse:
    crop = request.crop.strip().title()
    district = request.district.strip().title()
    language = request.language.strip()
    is_tomato = crop.lower() == "tomato"

    disease_summary = (
        "Possible early blight risk from yellow leaf spots. Image upload should confirm severity."
        if is_tomato
        else f"Run image diagnosis before deciding treatment for {crop}."
    )
    weather_summary = "Humidity is expected to be high, so fungal risk can increase in the evening."
    market_summary = f"{crop} price signal is mildly positive near {district}; avoid panic selling."

    summary = (
        f"{crop} advisory for {district}: {disease_summary} "
        f"{weather_summary} {market_summary}"
    )

    return AdvisoryResponse(
        crop=crop,
        district=district,
        language=language,
        summary=summary,
        overall_confidence=0.86 if is_tomato else 0.78,
        recommendations=[
            Recommendation(
                title="Verify disease symptoms",
                detail="Upload a clear leaf image and compare spots on older and younger leaves.",
                priority="high",
            ),
            Recommendation(
                title="Reduce fungal spread",
                detail="Avoid overhead watering and spray only after checking local advisory rules.",
                priority="medium",
            ),
            Recommendation(
                title="Check market timing",
                detail="If storage is available, wait 2-3 days and compare mandi price movement.",
                priority="medium",
            ),
        ],
        agent_results=[
            AgentResult(
                agent="Disease Agent",
                status="mocked",
                summary=disease_summary,
                confidence=0.88 if is_tomato else 0.72,
            ),
            AgentResult(
                agent="Weather Agent",
                status="mocked",
                summary=weather_summary,
                confidence=0.84,
            ),
            AgentResult(
                agent="Market Agent",
                status="mocked",
                summary=market_summary,
                confidence=0.76,
            ),
        ],
    )

