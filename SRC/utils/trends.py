import numpy as np
import pandas as pd
from utils.old_slope import compute_slope_betwween_2_points


def get_trends_events(
    df: pd.DataFrame, cols: list[str], degre: int, show_curve: bool = False
):
    """Get trends with polynomial feature"""
    x = df.index.values
    all_slope = {}
    for col in cols:
        y = df[col]
        coefficients = np.polyfit(x, y, degre)

        # Créer un modèle polynomial à partir des coefficients
        polynome = np.poly1d(coefficients)

        # Calculer les valeurs lissées
        y_lisse = polynome(x)

        first_day = x[0]
        last_day = x[-1]

        first_value = y_lisse[0]
        last_value = y_lisse[-1]

        slope = compute_slope_betwween_2_points(
            x1=first_day, y1=first_value, x2=last_day, y2=last_value
        )
        all_slope[col + "_slope"] = float(slope)

    return all_slope
