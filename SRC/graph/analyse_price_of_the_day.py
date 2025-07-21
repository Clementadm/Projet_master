import plotly.graph_objects as go
import pandas as pd


def make_indicator(
    label: str,
    trend_text: str,
    color: str,
    row_number: int,
    col_number: int,
    background_color: str = "white",
) -> go.Indicator:
    """
    Create an indicator graph that displays only a colored text string, without showing any numeric value.
    The numerical value is hidden by setting its font color to white (matching the background),
    while the trend text is styled using the specified color

    Input:
        - label: The label describing the indicator (displayed below the trend text).
        - trend_text: The trend text to display (e.g., "Bullish", "Down", etc.).
        - color: The color to apply to the trend text.
        - row_number: number of the row where the graph will be display
        - col_number: number of the col where the graph will be display
        - background_color : the color for the number value

    Output:
        - go.Indicator: A Plotly Indicator object with formatted text and hidden numeric value.
    """
    return go.Indicator(
        mode="number",  # Force to put one
        value=0,  # neutral value
        number={"font": {"color": background_color}},  # make it invisible
        title={
            "text": f"<span style='font-size:13px'>{label}</span><br><span style='color:{color}; font-size:20px; font-weight:bold'>{trend_text}</span>"
        },
        domain={"row": row_number, "column": col_number},
    )


def price_and_volume_kpi(
    df: pd.DataFrame, col_price: str, col_volume: str, background_color: str, width:int=450, height:int=100
) -> go.Figure:
    """
    Display two KPI indicators using Plotly: one for the price trend and one for the volume trend.
    The indicators are styled with color-coded text and arrow to visually represent the current state,
    and the numerical value is hidden by matching the background color.

    Inputs:
        - col_price: Column name in the DataFrame representing the price trend.
        - col_volume: Column name in the DataFrame representing the volume trend.
        - background_color: Background color used to hide the number value.
        - width: with of the return figure
        - height: height of the return figure

    Output:
        - go.Figure: A Plotly figure containing the two styled indicators.
    """
    # Mapping de couleur
    color_map = {
        "Up": "forestgreen",
        "Down": "firebrick",
        "Bearish": "firebrick",
        "Bullish": "forestgreen",
        "Stagnant": "dimgrey",
        "Very bearish": "darkred",
        "Very bullish": "darkgreen",
    }
    icon_map = {
        "Up": "⇧",
        "Down": "⇩",
        "Bearish": "↘",
        "Bullish": "↗",
        "Stagnant": "→",
        "Very bearish": "⇩",
        "Very bullish": "⇧",
    }
    fig = go.Figure()

    df = df.reset_index(drop=True)
    # price
    price_value = df.loc[0, col_price]
    # volume
    volume_value = df.loc[0, col_volume]

    fig.add_trace(
        make_indicator(
            label="Price trend",  # col_price.replace("_", " ").title(),
            trend_text=price_value + " " + icon_map.get(price_value, "black"),
            color=color_map.get(price_value, "black"),
            row_number=0,
            col_number=0,
            background_color=background_color,
        )
    )

    fig.add_trace(
        make_indicator(
            label="Volume",  # col_volume.replace("_", " ").title(),
            trend_text=volume_value + " " + icon_map.get(volume_value, "black"),
            color=color_map.get(volume_value, "black"),
            row_number=0,
            col_number=1,
            background_color=background_color,
        )
    )

    fig.update_layout(
        width=width,
        height=height,
        margin=dict(
            l=15,
            r=15,
            b=1,
            t=48,
            # pad=4
        ),
        paper_bgcolor=background_color,
        grid={"rows": 1, "columns": 2, "pattern": "independent"},
    )
    # fig.show()
    return fig


# for the day
# idincateur = pd.read_json(output_data["historical_stock_info"]["today_analyse_price"])
# df = idincateur.reset_index(drop=True)
# price_and_volume_kpi(
#     df = df,
#     col_price = "this_month_trend",
#     col_volume = "this_month_volume",
#     background_color = "lightgray"
# )
