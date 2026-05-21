from schemas import AgentResult


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

