from schemas import AgentResult


DISTRICT_WEATHER_NOTES = {
    "Nashik": "Humidity is expected to be high, so fungal risk can increase in the evening.",
    "Pune": "Light rain chances may increase leaf wetness risk during late evening.",
    "Indore": "Warm afternoon conditions can stress crops; inspect moisture before spraying.",
    "Ludhiana": "Cooler night conditions may slow disease spread but morning dew needs monitoring.",
    "Guntur": "Heat and humidity together can raise pest and fungal pressure.",
}


def run_weather_agent(crop: str, district: str) -> AgentResult:
    summary = DISTRICT_WEATHER_NOTES.get(
        district,
        f"Weather risk for {crop} in {district} should be checked before field action.",
    )

    return AgentResult(
        agent="Weather Agent",
        status="mocked",
        summary=summary,
        confidence=0.84,
    )

