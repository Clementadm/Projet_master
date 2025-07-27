import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from ihm.graph.news_table import get_news


def company_news(json_data, type):
    if type == "company_news":
        title = "Company News & Sentiment Analysis"
    elif type == "country_news":
        title = "Country News & Sentiment Analysis"
    st.markdown(
        f"<h3 style='text-align: center; color: #FE5D26;text-decoration: underline'>{title}</h3>",
        unsafe_allow_html=True,
    )
    company_news = get_news(
        json_data["news"][type],
    )
    st.write("---")
    date_min = pd.to_datetime(company_news["publishedAt"].min())
    date_max = pd.to_datetime(company_news["publishedAt"].max())
    duree = date_max - date_min
    col = st.columns((2.5, 2.5, 2.5), gap="large")
    with col[0]:
        st.text("")
        st.markdown(
            "<h5 style='color: #FE5D26;text-align:center'>📅 Publication period</h5>",
            unsafe_allow_html=True,
        )
        st.metric(
            label="",
            value=f"{date_min.strftime('%d %b %Y')} → {date_max.strftime('%d %b %Y')}",
            delta=f"{duree.days} jours",
            label_visibility="hidden",
        )
    with col[1]:
        st.markdown(
            "<h5 style='color: #FE5D26;'>Number of article</h5>",
            unsafe_allow_html=True,
        )
        number_of_news_article = company_news.shape[0]
        st.metric(label="", value=number_of_news_article, label_visibility="hidden")
    with col[2]:
        st.markdown(
            "<h5 style='color: #FE5D26;text-align:center'>News sentiment analyse</h5>",
            unsafe_allow_html=True,
        )

    st.write("---")  # st.text("")
    st.data_editor(
        company_news,
        column_config={
            "url": st.column_config.LinkColumn("url"),
            **{
                col: st.column_config.Column(width="small")
                for col in company_news.columns
                if col != "url"
            },
        },
        hide_index=True,
        height=800,
        num_rows="fixed",
        use_container_width=True,
    )
