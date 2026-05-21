from fastapi import File, Form, HTTPException, UploadFile, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from orchestrator import create_advisory
from schemas import AdvisoryRequest, AdvisoryResponse, DiseaseAnalysisResponse
from services.disease_agent import analyze_crop_image


app = FastAPI(
    title="Agri-AI Backend",
    description="Software-only multi-agent backend for agricultural decision-making.",
    version="0.2.0",
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
def advisory(request: AdvisoryRequest) -> AdvisoryResponse:
    return create_advisory(request)


@app.post("/disease/analyze", response_model=DiseaseAnalysisResponse)
async def analyze_disease_image(
    crop: str = Form(default="Tomato"),
    image: UploadFile = File(...),
) -> DiseaseAnalysisResponse:
    if image.content_type and not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload an image file.")

    image_bytes = await image.read()
    if not image_bytes:
        raise HTTPException(status_code=400, detail="Uploaded image is empty.")

    return analyze_crop_image(
        crop=crop,
        filename=image.filename or "crop-image",
        content_type=image.content_type,
        image_size=len(image_bytes),
    )
