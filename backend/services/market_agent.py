from schemas import AgentResult


CROP_MARKET_SIGNALS = {
    "Tomato": "Tomato price signal is mildly positive near {district}; avoid panic selling.",
    "Onion": "Onion prices are volatile near {district}; compare two nearby mandis before selling.",
    "Wheat": "Wheat price is stable near {district}; selling can be planned around transport cost.",
    "Rice": "Rice demand is steady near {district}; monitor quality grade before final sale.",
    "Cotton": "Cotton price trend is mixed near {district}; wait for a clearer buyer quote if possible.",
}


def run_market_agent(crop: str, district: str) -> AgentResult:
    template = CROP_MARKET_SIGNALS.get(
        crop,
        f"{crop} price signal is mildly positive near {{district}}; avoid panic selling.",
    )

    return AgentResult(
        agent="Market Agent",
        status="mocked",
        summary=template.format(district=district),
        confidence=0.76,
    )

