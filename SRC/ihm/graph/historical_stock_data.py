import plotly.graph_objects as go
import pandas as pd
import numpy as np


def historic_stock_candle_stick_chart(
    df: pd.DataFrame,
    height: int,
    width: int,
    increasing_color: str = "#3D9970",
    decreasing_color: str = "#FF4136",
):
    """
    Generate a candlestick chart to visualize historical stock price movements.

    This function takes a DataFrame containing historical stock data and create
    a Plotly candlestick chart, with customizable colors for increasing and
    decreasing candles, as well as figure dimensions.

    Input:
        - df: DataFrame containing 'Date', 'Open', 'High', 'Low', 'Close' columns.
        - increasing_color: Color for upward candles (default: "3D9970").
        - decreasing_color: Color for downward candles (default: "FF4136").
        - height: Height of the figure in pixels.
        - width: Width of the figure in pixels.

    Output:
        go.Figure: A Plotly Figure object representing the candlestick chart.
    """

    fig = go.Figure(
        data=[
            go.Candlestick(
                x=df["Date"],
                open=df["Open"],
                high=df["High"],
                low=df["Low"],
                close=df["Close"],
            )
        ]
    )

    fig.data[0].increasing.fillcolor = increasing_color
    fig.data[0].increasing.line.color = increasing_color
    fig.data[0].decreasing.fillcolor = decreasing_color
    fig.data[0].decreasing.line.color = decreasing_color

    fig.update_layout(
        title={
                'text': "Historical Stock Performance",
                'font': {'color': '#FFD700'}
        },
        xaxis_title="Date",
        yaxis_title="Price",
        height=height,
        width=width,
        margin=dict(l=50, r=5, b=35, t=25, pad=4),
        # paper_bgcolor="LightSteelBlue",
    )

    return fig


# second graph
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


def get_trends_events_graph(
    df: pd.DataFrame,
    cols: list[str],
    degre: int,
    height: int,
    width: int,
    show_curve: bool = False,
    colors: dict[str, str] = None,
):
    """
    Analyze trends in selected columns of a DataFrame by fitting polynomial regressions,
    optionally displaying the original and smoothed curves using Plotly.

    Inputs:
        - df: Input DataFrame with a 'Date' column and columns to be analyzed.
        - cols: List of column names from `df` for which to compute trends.
        - degre: Degree of the polynomial regression to fit.
        - height: Height of the resulting figure (if `show_curve` is True).
        - width: Width of the resulting figure (if `show_curve` is True).
        - show_curve: If True, returns a Plotly figure showing the data and polynomial fit.
        - colors: Dictionary mapping column names to specific colors.

    Outputs:
        - If show_curve is True: returns a Plotly `go.Figure` object with the plotted trends.
        - Else: returns a dictionary with the computed slopes for each selected column.
    """
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
            fig.add_trace(
                go.Scatter(
                    x=df["Date"],  # .apply(lambda x : str(x.date())),
                    y=y,
                    mode="markers",
                    name=f"{col} - Observé",
                    marker=dict(color=color),
                    opacity=0.5,
                )
            )

            # Régression polynomiale
            fig.add_trace(
                go.Scatter(
                    x=df["Date"],  # .apply(lambda x : str(x.date())),
                    y=y_lisse,
                    mode="lines",
                    name=f"{col} - polynomial modeling of {degre}",
                    line=dict(color=color),
                )
            )

    if show_curve:
        fig.update_layout(
            title={
                'text': "Overview of Market Trends and Polynomial Modeling",
                'font': {'color': '#FFD700'}
            },
            xaxis_title="Date",
            yaxis_title="Price",
            height=height,
            width=width,
            margin=dict(l=10, r=10, b=10, t=50, pad=4),
            legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5)
        )
        return fig

    return return_slop
