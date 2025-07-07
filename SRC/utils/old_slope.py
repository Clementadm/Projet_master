from typing import Dict


def compute_slope_betwween_2_points(
    x1: float, y1: float, x2: float, y2: float
) -> float:
    #  coefficient directeur
    """
    Calculates the directing coefficient (slope) of a line passing through two points.

    Args:
        x1 (float): x coordinate of first point.
        y1 (float): y coordinate of first point.
        x2 (float): x coordinate of second point.
        y2 (float): Y coordinate of the second point.

    Returns:
        float: The directing coefficient of the line.
    """
    if x1 == x2:
        raise ValueError(
            "The points have the same x coordinate. The line is vertical and its slope is indefinite."
        )

    slope = (y2 - y1) / (x2 - x1)
    # print(f"Calcul ==> ({y2} - {y1}) / ({x2} - {x1})")
    return slope


def qualify_slope(coefficient: float) -> Dict[str, str]:
    """
    Classifies the steepness and direction of a slope based on its coefficient.
        - -0.3 < m < 0.3: Nearly flat → considered stagnant
        - m = 0: Perfectly flat (stagnant)
        - 0.3 ≤ m < 1: Moderately increasing → bullish
        - m ≥ 1: Strongly increasing → very bullish
        - -1 < m ≤ -0.3: Moderately decreasing → bearish
        - m ≤ -1: Strongly decreasing → very bearish

    These thresholds are empirically chosen to reflect intuitive and visual perception
    of slope steepness,

    Args:
        m (float): The slope coefficient.

    Returns:
        str: A label describing the slope: Very bullish, Bullish, Stagnant, Bearish, Very bearish
    """
    if coefficient >= 1:
        return {"steepness": "Very bullish"}
    elif 0.15 <= coefficient < 1:
        return {"steepness": "Bullish"}
    elif -0.15 < coefficient < 0.15:
        return {"steepness": "Stagnant"}
    elif -1 < coefficient <= -0.15:
        return {"steepness": "Bearish"}
    else:
        return {"steepness": "Very bearish"}
