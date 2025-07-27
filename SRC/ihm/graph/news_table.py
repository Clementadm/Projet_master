import pandas as pd
import io
import plotly.graph_objects as go


def get_news(news_data: str) -> go.Figure:
    """
    Generate a styled dark-themed interactive Plotly table displaying company news with sentiment analysis.

    Parameters:
        news_data: JSON string containing the news data.

    Returns:
        dataframe to plot on streamlit
    """

    df_news = pd.read_json(io.StringIO(news_data))
    df_news["publishedAt"] = pd.to_numeric(df_news["publishedAt"], errors='coerce')
    df_news["publishedAt"] = pd.to_datetime(df_news["publishedAt"], unit='ms')

    df_news = df_news[["publishedAt", "headline", "summary", "source", "url", "sentiment"]].copy()
    df_news["sentiment"] = df_news["sentiment"].apply(lambda x: "🟢 positif" if x == 1 else "🔴 negatif")

    return df_news