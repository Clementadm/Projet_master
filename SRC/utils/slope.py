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
