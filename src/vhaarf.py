"""Pre-adoption V-HAARF recommendation from three 1-5 layer scores."""


def mean_layers(l1: float, l2: float, l3: float) -> float:
    return (l1 + l2 + l3) / 3.0


def recommend(l1: float, l2: float, l3: float) -> str:
    m = mean_layers(l1, l2, l3)
    if m >= 3.5:
        return "agentic_ai_pilot"
    if m >= 2.5:
        return "traditional_automation"
    return "human_led"
