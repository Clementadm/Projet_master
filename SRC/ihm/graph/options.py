from typing import List
import plotly.graph_objects as go
from ihm.graph.analyse_price_of_the_day import make_indicator
from plotly.subplots import make_subplots


def bar_chart_options(
    background_color: str,
    left_bar_y_buy: List[float],
    left_bar_y_sell: List[float],
    left_title: str,
    left_yaxis_title: str,
    right_bar_y_buy: List[float],
    right_bar_y_sell: List[float],
    right_title: str,
    right_yaxis_title: str,
    width: int = 500,
    height: int = 150,
) -> go.Figure:
    """
        Creates a dual bar chart with two subplots showing buy/sell volumes and counts.

    Args:
        background_color: Background color of the chart
        left_bar_y_buy (List[float]): Y-values for 'Buy' bar in the left subplot.
        left_bar_y_sell (List[float]): Y-values for 'Sell' bar in the left subplot.
        left_title (str): Title of the left subplot.
        left_yaxis_title (str): Y-axis label for the left subplot.
        right_bar_y_buy (List[float]): Y-values for 'Buy' bar in the right subplot.
        right_bar_y_sell (List[float]): Y-values for 'Sell' bar in the right subplot.
        right_title (str): Title of the right subplot.
        right_yaxis_title (str): Y-axis label for the right subplot.
        width: with of the return figure
        height: height of the return figure

    Returns:
        Figure: Plotly Figure with two bar charts.
    """

    fig = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=(left_title, right_title),
        horizontal_spacing=0.30,
    )

    # Left chart ==> Volume option
    fig.add_trace(
        go.Bar(
            name="Buy",
            x=["Buy"],
            y=left_bar_y_buy,
            marker_color="forestgreen",
            showlegend=False,
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Bar(
            name="Sell",
            x=["Sell"],
            y=left_bar_y_sell,
            marker_color="firebrick",
            showlegend=False,
        ),
        row=1,
        col=1,
    )

    # Right chart ==> Number of options
    fig.add_trace(
        go.Bar(
            name="Buy",
            x=["Buy"],
            y=right_bar_y_buy,
            marker_color="forestgreen",
            showlegend=False,
        ),
        row=1,
        col=2,
    )
    fig.add_trace(
        go.Bar(
            name="Sell",
            x=["Sell"],
            y=right_bar_y_sell,
            marker_color="firebrick",
            showlegend=False,
        ),
        row=1,
        col=2,
    )

    fig.update_layout(
        width=width,
        height=height,
        showlegend=False,
        margin=dict(
            l=40,  # 15,
            r=40,  # 15,
            b=1,  # 1,
            t=0,  # 48,
        ),
        paper_bgcolor=background_color,
        grid={"rows": 1, "columns": 2, "pattern": "independent"},
        yaxis=dict(title=left_yaxis_title, title_standoff=5),
        yaxis2=dict(title=right_yaxis_title, title_standoff=5),
    )
    return fig


# bar_chart_options(
#     graph_title= "Buy/Sell options Comparison",
#     # left
#     left_bar_y_buy=data["buy_mean_volume"], left_bar_y_sell=data["sell_mean_volume"],
#     left_title="Mean options volume",
#     left_yaxis_title="Volume",


#     right_bar_y_buy= data["nb_option_buy"], right_bar_y_sell=data["nb_option_sell"],
#     right_title="Number of different options",
#     right_yaxis_title="Number of options"
# )


def graph_comparate_actual_price_with_option_price(
    cluster_buy: str,
    cluster_sell: str,
    background_color: str,
    width: int = 450,
    height: int = 50,
) -> go.Figure:
    """
    Generates a dual-indicator Plotly chart comparing buy and sell option price clusters.
    Each cluster is visually styled based on its valuation category using a predefined color mapping.

    Args:
        cluster_buy: Valuation label for the buy option price
        cluster_sell: Valuation label for the sell option price
        background_color: Background color of the chart
        width: with of the return figure
        height: height of the return figure

    Returns:
        go.Figure: A Plotly figure object containing two side-by-side indicators.
    """
    # Mapping de couleur
    color_map = {
        "Very undervalued": "darkgreen",
        "Slightly undervalued": "forestgreen",  # green
        "Price within spread": "dimgrey",
        "Slightly overvalued": "firebrick",  # red
        "Very overvalued": "darkred",
    }

    fig = go.Figure()
    fig.add_trace(
        make_indicator(
            label="Buy Price Option",  # col_price.replace("_", " ").title(),
            trend_text=cluster_buy,  # + " " + icon_map.get(cluster_buy, "black"),
            color=color_map.get(cluster_buy, "black"),
            row_number=0,
            col_number=0,
            background_color=background_color,
        )
    )

    fig.add_trace(
        make_indicator(
            label="Sell Price Option",  # col_volume.replace("_", " ").title(),
            trend_text=cluster_sell,  # + " " + icon_map.get(cluster_sell, "black"),
            color=color_map.get(cluster_sell, "black"),
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
        ),
        paper_bgcolor=background_color,
        grid={"rows": 1, "columns": 2, "pattern": "independent"},
    )

    return fig


# graph_comparate_actual_price_with_option_price(
#     cluster_buy = output_data["options"]["cluster_buy"][0],
#     cluster_sell = output_data["options"]["cluster_sell"][0],
#     background_color = "lightgray"
# )
