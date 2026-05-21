from schemas import AgentResult, DiseaseAnalysisResponse


def run_disease_agent(crop: str, question: str) -> AgentResult:
    normalized_question = question.lower()
    is_tomato = crop.lower() == "tomato"
    mentions_leaf_spots = "spot" in normalized_question or "yellow" in normalized_question

    if is_tomato and mentions_leaf_spots:
        summary = "Possible early blight risk from yellow leaf spots. Image upload should confirm severity."
        confidence = 0.88
    elif is_tomato:
        summary = "Tomato disease risk needs image confirmation before treatment advice."
        confidence = 0.78
    else:
        summary = f"Run image diagnosis before deciding treatment for {crop}."
        confidence = 0.72

    return AgentResult(
        agent="Disease Agent",
        status="mocked",
        summary=summary,
        confidence=confidence,
    )


def analyze_crop_image(crop: str, filename: str, content_type: str | None, image_size: int) -> DiseaseAnalysisResponse:
    normalized_crop = crop.strip().title()
    is_tomato = normalized_crop.lower() == "tomato"

    if is_tomato:
        disease = "Early Blight"
        confidence = 0.88
        severity = "medium"
        symptoms = [
            "Yellowing around older leaves",
            "Circular brown leaf spots",
            "Possible fungal spread under humid conditions",
        ]
        treatment = [
            "Remove heavily infected leaves from the field",
            "Use a recommended fungicide only after local advisory confirmation",
            "Avoid water splashing on leaves during irrigation",
        ]
        prevention = [
            "Keep spacing between plants for airflow",
            "Inspect lower leaves every 2-3 days",
            "Do not reuse infected plant residue as compost",
        ]
    else:
        disease = "General Leaf Stress"
        confidence = 0.74
        severity = "low"
        symptoms = [
            "Visible leaf discoloration needs closer inspection",
            "Image-based confirmation is recommended",
        ]
        treatment = [
            "Capture a clearer close-up leaf image",
            "Check soil moisture and recent spray history",
        ]
        prevention = [
            "Monitor crop weekly",
            "Avoid spraying during harsh afternoon heat",
        ]

    readable_size = f"{round(image_size / 1024, 1)} KB"

    return DiseaseAnalysisResponse(
        crop=normalized_crop,
        filename=filename,
        disease=disease,
        confidence=confidence,
        severity=severity,
        symptoms=symptoms,
        treatment=treatment,
        prevention=prevention,
        note=(
            f"Mock image analysis completed for a {content_type or 'file'} upload "
            f"({readable_size}). Replace this rule-based result with a trained model later."
        ),
    )
