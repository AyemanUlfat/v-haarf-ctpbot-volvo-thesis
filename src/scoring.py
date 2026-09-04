"""AI System Effectiveness Score.

overall_100 = 20 * (w1*L1 + w2*L2 + w3*L3)
when each Li is on a 1-5 scale.
"""

from __future__ import annotations


def weighted_layer_sum(l1: float, l2: float, l3: float, w1: float, w2: float, w3: float) -> float:
    return w1 * l1 + w2 * l2 + w3 * l3


def effectiveness_score_100(l1: float, l2: float, l3: float, weights: dict) -> float:
    s = weighted_layer_sum(
        l1,
        l2,
        l3,
        weights["L1_lifecycle_governance"],
        weights["L2_capability"],
        weights["L3_real_world_performance"],
    )
    return round(s * 20.0, 1)


def score_band(score_100: float) -> str:
    if score_100 >= 80:
        return "ready_for_wider_adoption"
    if score_100 >= 65:
        return "promising_needs_improvement"
    if score_100 >= 50:
        return "limited_pilot_only"
    return "not_recommended"
