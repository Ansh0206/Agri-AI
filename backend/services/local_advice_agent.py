from schemas import LocalAdviceResponse


def generate_local_advice(crop: str, district: str, language: str, question: str) -> LocalAdviceResponse:
    normalized_crop = crop.strip().title()
    normalized_district = district.strip().title()
    normalized_language = "Hindi" if language.strip().lower() == "hindi" else "English"

    if normalized_language == "Hindi":
        answer = (
            f"{normalized_crop} फसल के लिए {normalized_district} में सलाह: "
            "पत्तियों पर पीले धब्बे दिख रहे हैं तो पहले साफ पत्ती की फोटो अपलोड करें। "
            "पत्तों पर पानी न डालें, नमी ज्यादा हो तो फंगल रोग का खतरा बढ़ सकता है, "
            "और छिड़काव से पहले मौसम और स्थानीय सलाह जरूर जांचें।"
        )
        key_points = [
            "साफ पत्ती की फोटो अपलोड करें",
            "शाम को पत्तों को गीला न रखें",
            "मंडी भाव देखकर ही बिक्री का फैसला लें",
        ]
    else:
        answer = (
            f"For {normalized_crop} in {normalized_district}: upload a clear leaf photo first. "
            "If yellow spots are visible, avoid wetting the leaves, check humidity risk before spraying, "
            "and compare mandi prices before harvesting or selling."
        )
        key_points = [
            "Upload a clear leaf photo",
            "Avoid keeping leaves wet in the evening",
            "Check mandi trend before selling",
        ]

    return LocalAdviceResponse(
        crop=normalized_crop,
        district=normalized_district,
        language=normalized_language,
        answer=answer,
        key_points=key_points,
        confidence=0.82,
    )
