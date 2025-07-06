import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# from utils.slope import compute_slope_betwween_2_points


def candlestick_price_chart(df: pd.DataFrame):
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=df["Date"],
                open=df["Open"],
                high=df["High"],
                low=df["Low"],
                close=df["Close"],
                increasing_line_color='green', decreasing_line_color='red'
            )
        ]
    )
    fig.update_layout(
        xaxis_rangeslider_visible=True,
        title=dict(text="Price evolution"),
        yaxis=dict(title=dict(text="Stock Price")),
        xaxis=dict(title=dict(text="Date")),
    )
    fig.show()