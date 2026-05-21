from schemas import AgentResult, WeatherRiskResponse


DISTRICT_WEATHER_NOTES = {
    "Nashik": "Humidity is expected to be high, so fungal risk can increase in the evening.",
    "Pune": "Light rain chances may increase leaf wetness risk during late evening.",
    "Indore": "Warm afternoon conditions can stress crops; inspect moisture before spraying.",
    "Ludhiana": "Cooler night conditions may slow disease spread but morning dew needs monitoring.",
    "Guntur": "Heat and humidity together can raise pest and fungal pressure.",
}

DISTRICT_WEATHER_DATA = {
    "Nashik": {
        "temperature_c": 29,
        "humidity_percent": 82,
        "rain_chance_percent": 58,
        "wind_kmph": 11,
    },
    "Pune": {
        "temperature_c": 28,
        "humidity_percent": 74,
        "rain_chance_percent": 42,
        "wind_kmph": 13,
    },
    "Indore": {
        "temperature_c": 33,
        "humidity_percent": 51,
        "rain_chance_percent": 18,
        "wind_kmph": 16,
    },
    "Ludhiana": {
        "temperature_c": 25,
        "humidity_percent": 68,
        "rain_chance_percent": 25,
        "wind_kmph": 9,
    },
    "Guntur": {
        "temperature_c": 34,
        "humidity_percent": 79,
        "rain_chance_percent": 36,
        "wind_kmph": 14,
    },
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


def analyze_weather_risk(crop: str, district: str) -> WeatherRiskResponse:
    normalized_crop = crop.strip().title()
    normalized_district = district.strip().title()
    data = DISTRICT_WEATHER_DATA.get(
        normalized_district,
        {
            "temperature_c": 30,
            "humidity_percent": 65,
            "rain_chance_percent": 30,
            "wind_kmph": 12,
        },
    )

    humidity = data["humidity_percent"]
    rain_chance = data["rain_chance_percent"]
    temperature = data["temperature_c"]

    if humidity >= 80 or rain_chance >= 55:
        risk_level = "high"
        disease_pressure = "Fungal disease pressure is high because leaf wetness may stay longer."
        advice = "Avoid evening irrigation, inspect lower leaves, and delay spraying if rain is likely."
    elif humidity >= 65 or rain_chance >= 35:
        risk_level = "medium"
        disease_pressure = "Moderate fungal and pest pressure is possible under current conditions."
        advice = "Monitor crop canopy, keep spacing clear, and spray only in a safe weather window."
    elif temperature >= 33:
        risk_level = "medium"
        disease_pressure = "Heat stress can increase crop weakness even when fungal pressure is lower."
        advice = "Check soil moisture early morning and avoid afternoon spraying."
    else:
        risk_level = "low"
        disease_pressure = "Weather-driven disease pressure is currently low."
        advice = "Continue routine scouting and keep field records updated."

    return WeatherRiskResponse(
        crop=normalized_crop,
        district=normalized_district,
        temperature_c=temperature,
        humidity_percent=humidity,
        rain_chance_percent=rain_chance,
        wind_kmph=data["wind_kmph"],
        risk_level=risk_level,
        disease_pressure=disease_pressure,
        advice=advice,
        next_24_hours=[
            "Morning: scout lower leaves and check soil moisture.",
            "Afternoon: avoid spraying during harsh heat or wind.",
            "Evening: reduce leaf wetness if humidity remains high.",
        ],
    )
