from schemas import AgentResult, MarketPriceResponse, PricePoint


CROP_MARKET_SIGNALS = {
    "Tomato": "Tomato price signal is mildly positive near {district}; avoid panic selling.",
    "Onion": "Onion prices are volatile near {district}; compare two nearby mandis before selling.",
    "Wheat": "Wheat price is stable near {district}; selling can be planned around transport cost.",
    "Rice": "Rice demand is steady near {district}; monitor quality grade before final sale.",
    "Cotton": "Cotton price trend is mixed near {district}; wait for a clearer buyer quote if possible.",
}

MARKET_DATA = {
    ("Tomato", "Nashik"): {
        "mandi": "Nashik APMC",
        "today_price": 1850,
        "yesterday_price": 1705,
        "history": [1540, 1600, 1660, 1705, 1850],
    },
    ("Onion", "Nashik"): {
        "mandi": "Lasalgaon Mandi",
        "today_price": 2320,
        "yesterday_price": 2470,
        "history": [2210, 2290, 2390, 2470, 2320],
    },
    ("Wheat", "Ludhiana"): {
        "mandi": "Ludhiana Grain Market",
        "today_price": 2260,
        "yesterday_price": 2245,
        "history": [2220, 2235, 2240, 2245, 2260],
    },
    ("Rice", "Guntur"): {
        "mandi": "Guntur Market Yard",
        "today_price": 3180,
        "yesterday_price": 3185,
        "history": [3160, 3175, 3190, 3185, 3180],
    },
    ("Cotton", "Indore"): {
        "mandi": "Indore Cotton Market",
        "today_price": 7020,
        "yesterday_price": 6940,
        "history": [6810, 6875, 6900, 6940, 7020],
    },
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


def analyze_market_price(crop: str, district: str) -> MarketPriceResponse:
    normalized_crop = crop.strip().title()
    normalized_district = district.strip().title()
    data = MARKET_DATA.get(
        (normalized_crop, normalized_district),
        {
            "mandi": f"{normalized_district} Local Mandi",
            "today_price": 1800,
            "yesterday_price": 1760,
            "history": [1650, 1690, 1720, 1760, 1800],
        },
    )

    today_price = data["today_price"]
    yesterday_price = data["yesterday_price"]
    change_percent = round(((today_price - yesterday_price) / yesterday_price) * 100, 1)

    if change_percent >= 3:
        trend = "rising"
        advice = "Hold for 2-3 days if storage is available, but confirm prices in nearby mandis."
    elif change_percent <= -3:
        trend = "falling"
        advice = "Consider selling in smaller lots or compare buyer quotes before waiting longer."
    else:
        trend = "stable"
        advice = "Price is stable; sell based on quality, transport cost, and storage condition."

    labels = ["4 days ago", "3 days ago", "2 days ago", "Yesterday", "Today"]

    return MarketPriceResponse(
        crop=normalized_crop,
        district=normalized_district,
        mandi=data["mandi"],
        today_price=today_price,
        yesterday_price=yesterday_price,
        unit="Rs/quintal",
        trend=trend,
        change_percent=change_percent,
        advice=advice,
        price_history=[
            PricePoint(label=label, price=price)
            for label, price in zip(labels, data["history"], strict=True)
        ],
    )
