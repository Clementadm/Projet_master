from typing import Dict, Any
import plotly.graph_objects as go


def analyst_price_recommendation(
    options_data: Dict[str, Any],
    background_color: str,
    width: int = 500,
    height: int = 150,
) -> go.Figure:
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=options_data["current_price"],
            gauge={
                "axis": {
                    "range": [
                        options_data["low_analyst_price_targets"],
                        options_data["high_analyst_price_targets"],
                    ]
                },
                "bar": {"color": "black"},
                "steps": [
                    {
                        "range": [
                            options_data["low_analyst_price_targets"],
                            options_data["median_analyst_price_targets"],
                        ],
                        "color": "darkorange",
                    },
                    {
                        "range": [
                            options_data["median_analyst_price_targets"],
                            options_data["mean_analyst_price_targets"],
                        ],
                        "color": "dimgrey",
                    },
                    {
                        "range": [
                            options_data["mean_analyst_price_targets"],
                            options_data["high_analyst_price_targets"],
                        ],
                        "color": "forestgreen",
                    },
                ],
                "threshold": {
                    "line": {"color": "red", "width": 4},
                    "thickness": 0.75,
                    "value": options_data["current_price"],
                },
            },
        )
    )

    # Add an legend for each colors
    fig.add_trace(
        go.Scatter(
            x=[None],
            y=[None],
            mode="markers",
            marker=dict(size=12, color="darkorange"),
            name="LOWEST price to MEDIAN price",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[None],
            y=[None],
            mode="markers",
            marker=dict(size=12, color="dimgrey"),
            name="MEDIAN price to MEAN price",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[None],
            y=[None],
            mode="markers",
            marker=dict(size=12, color="forestgreen"),
            name="MEAN price to HIGHEST price",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[None],
            y=[None],
            mode="markers",
            marker=dict(size=12, color="red"),
            name="Actual price",
        )
    )

    fig.update_layout(
        width=width,
        height=height,
        paper_bgcolor=background_color,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        legend=dict(
            orientation="v",  # vertical
            yanchor="top",
            y=0.7,
            xanchor="left",
            x=1.1,  # shift legend to the left
            bgcolor="rgba(0,0,0,0)",  # no legend background
        ),
        margin=dict(t=0, b=0, l=5, r=0),
    )

    return fig


# analyst_price_recommendation(output_data["options"])


def breakdown_of_sentiment_analyst(
    sentiment_analyst: dict[str, float], height=100, width=400
) -> go.Figure:
    """
    Generates a donut chart showing the distribution of positive and negative analyst sentiments.

    Args:
        - sentiment_analyst : Dictionary containing sentiment values with keys 'positif' and 'negatifs' (values between 0 and 1 or as percentages).
        - width: with of the return figure
        - height: height of the return figure

    Returns:
        fig: A Plotly donut chart visualizing positive vs. negative analyst sentiment.
    """
    positive_sentiment = round(float(sentiment_analyst["positif"]), 1)
    negative_sentiment = round(float(sentiment_analyst["negatifs"]), 1)

    labels = ["Positive", "Negative"]
    values = [positive_sentiment, negative_sentiment]
    colors = ["forestgreen", "firebrick"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                marker=dict(colors=colors),
                textinfo="percent",
                hole=0.65,  # 0 = full pie, 0.5 = donut
                hoverinfo="label+percent",
            )
        ]
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=True,
        height=height,
        width=width,
        margin=dict(t=0, b=0, l=5, r=0),
    )

    return fig


# breakdown_of_sentiment_analyst(output_data["historical_stock_info"]["breakdown_of_analyst_recommendation"]["distribution_of_recommendations"])
