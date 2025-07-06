import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

def get_trends_events(
    df: pd.DataFrame,
    cols: list[str],
    degre: int,
    show_curve: bool = False,
    colors: dict[str, str] = None
):
    x = df.index.values
    return_slop = {}

    if show_curve:
        fig = go.Figure()

    for col in cols:
        y = df[col].values
        coefficients = np.polyfit(x, y, degre)
        polynome = np.poly1d(coefficients)
        y_lisse = polynome(x)

        first_day, last_day = x[0], x[-1]
        first_value, last_value = y_lisse[0], y_lisse[-1]

        slope = compute_slope_betwween_2_points(
            x1=first_day, y1=first_value, x2=last_day, y2=last_value
        )

        return_slop[col + "_slope"] = slope

        if show_curve:
            color = colors.get(col) if colors else None

            # Points observés
            fig.add_trace(go.Scatter(
                x=df["Date"].apply(lambda x : str(x.date())),
                y=y,
                mode='markers',
                name=f"{col} - Observé",
                marker=dict(color=color),
                opacity=0.5
            ))

            # Régression polynomiale
            fig.add_trace(go.Scatter(
                x=df["Date"].apply(lambda x: str(x.date())),
                y=y_lisse,
                mode='lines',
                name=f"{col} - Régression degré {degre}",
                line=dict(color=color)
            ))

    if show_curve:
        fig.update_layout(
            title="Courbes de régression polynomiale",
            xaxis_title="Date",
            yaxis_title="Price",
            height=600,
            width=1000
        )
        fig.show()

    return return_slop

