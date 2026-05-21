from schemas import AdvisoryRequest, AdvisoryResponse, Recommendation
from services.disease_agent import run_disease_agent
from services.market_agent import run_market_agent
from services.weather_agent import run_weather_agent


def create_advisory(request: AdvisoryRequest) -> AdvisoryResponse:
    crop = request.crop.strip().title()
    district = request.district.strip().title()
    language = request.language.strip()

    disease_result = run_disease_agent(crop=crop, question=request.question)
    weather_result = run_weather_agent(crop=crop, district=district)
    market_result = run_market_agent(crop=crop, district=district)

    agent_results = [disease_result, weather_result, market_result]
    overall_confidence = round(
        sum(result.confidence for result in agent_results) / len(agent_results),
        2,
    )

    summary = (
        f"{crop} advisory for {district}: {disease_result.summary} "
        f"{weather_result.summary} {market_result.summary}"
    )

    return AdvisoryResponse(
        crop=crop,
        district=district,
        language=language,
        summary=summary,
        overall_confidence=overall_confidence,
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
        agent_results=agent_results,
    )

