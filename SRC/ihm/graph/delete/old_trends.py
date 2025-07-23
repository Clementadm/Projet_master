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


def get_trends_events(x: pd.Series, y: pd.Series, degre: int, show_curve: bool = False):
    coefficients = np.polyfit(x, y, degre)

    # Créer un modèle polynomial à partir des coefficients
    polynome = np.poly1d(coefficients)

    # Calculer les valeurs lissées
    y_lisse = polynome(x)

    first_day = x[0]
    last_day = x[-1]

    first_value = y_lisse[0]
    last_value = y_lisse[-1]
    print(f"x1={first_day}, y1={first_value}, x2={last_day}, y2={last_value}")

    slope = compute_slope_betwween_2_points(
        x1=first_day, y1=first_value, x2=last_day, y2=last_value
    )

    if show_curve:
        # Tracer les données originales et la courbe lissée
        plt.scatter(x, y, color="blue", label="Points observés")
        plt.plot(
            x, y_lisse, color="red", label=f"Régression polynomiale de degré {degre}"
        )
        # plt.set_xticklabels(df["Date_str"], rotation=90)
        plt.legend()
    return {
        "first_day": first_day,
        "last_day": last_day,
        "first_value": first_value,
        "last_value": last_value,
        "slope": slope,
    }


# __________________________________________________________________________________
# def get_trends_events(df: pd.DataFrame, cols: list[str], degre: int, show_curve: bool = False):
#     x = df.index.values
#     for col in cols:
#         y = df[col]
#         coefficients = np.polyfit(x, y, degre)

#         # Créer un modèle polynomial à partir des coefficients
#         polynome = np.poly1d(coefficients)

#         # Calculer les valeurs lissées
#         y_lisse = polynome(x)

#         first_day = x[0]
#         last_day = x[-1]

#         first_value = y_lisse[0]
#         last_value = y_lisse[-1]
#         print(f"x1={first_day}, y1={first_value}, x2={last_day}, y2={last_value}")

#         slope = compute_slope_betwween_2_points(
#             x1=first_day, y1=first_value, x2=last_day, y2=last_value
#         )


#     if show_curve:
#         # Tracer les données originales et la courbe lissée
#         plt.scatter(x, y, color="blue", label="Points observés")
#         plt.plot(
#             x, y_lisse, color="red", label=f"Régression polynomiale de degré {degre}"
#         )
#         # plt.set_xticklabels(df["Date_str"], rotation=90)
#         plt.legend()
#     return {
#         "first_day": first_day,
#         "last_day": last_day,
#         "first_value": first_value,
#         "last_value": last_value,
#         "slope": slope
#     }


# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd


def get_trends_events(
    df: pd.DataFrame,
    cols: list[str],
    degre: int,
    show_curve: bool = False,
    colors: dict[str, str] = None,
):
    x = df.index.values

    return_slop = {}

    if show_curve:
        _, ax = plt.subplots(figsize=(14, 7))

    for col in cols:
        y = df[col]
        coefficients = np.polyfit(x, y, degre)

        # Créer un modèle polynomial à partir des coefficients
        polynome = np.poly1d(coefficients)
        y_lisse = polynome(x)

        first_day = x[0]
        last_day = x[-1]
        first_value = y_lisse[0]
        last_value = y_lisse[-1]

        slope = compute_slope_betwween_2_points(
            x1=first_day, y1=first_value, x2=last_day, y2=last_value
        )

        if show_curve:
            color = colors.get(col, None) if colors else None
            ax.scatter(x, y, label=f"{col} - Observé", alpha=0.5, color=color)
            ax.plot(x, y_lisse, label=f"{col} - Régression degré {degre}", color=color)

        return_slop[col + "_slope"] = slope

    if show_curve:
        ax.legend(df["Date"])
        ax.set_xticklabels(df["Date"].apply(lambda x: str(x.date())), rotation=90)
        ax.set_ylim(first_value - 10, last_value + 10)
        ax.set_ylabel("Price")
        ax.set_xlabel("Date")
        ax.set_title("Courbes de régression polynomiale")
        plt.tight_layout()
        plt.show()

    return return_slop
