import streamlit as st
from ihm.graph.analyse_price_of_the_day import price_and_volume_kpi
import pandas as pd
from io import StringIO
from ihm.utils.read_json_file import read_json_file

# from datetime import datetime
from ihm.graph.historical_stock_data import (
    historic_stock_candle_stick_chart,
    get_trends_events_graph,
)
from ihm.utils.get_data_from_choosen_company import get_data_of_choosen_company

st.set_page_config(
    page_title="Projet IA Bourse",
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="expanded",
)

streamlit_background_color = "#0e1117"
company_dict = {
    "Microsoft": "msft",
    "Pfizer": "pfe",
    "Abercrombie & Fitch": "anf",
    "Starbucks": "sbux",
    "Tesla": "tsla",
    "Walmart": "wmt",
}

only_company_name = list(company_dict.keys())
choosen_company = st.selectbox("Choose an company to analyse", only_company_name)

if choosen_company is not None:
    print(f"Choosen_company: {choosen_company}")

    # get the data from lastest json file of the company select
    latest_file = get_data_of_choosen_company(company_dict, choosen_company)
    json_data = read_json_file(file_name=latest_file)
    today_analyse_price_data = pd.read_json(
        StringIO(json_data["historical_stock_info"]["today_analyse_price"])
    )

    col = st.columns((2, 4.5, 2), gap="medium")  # , vertical_alignment="center")
    with col[0]:
        # title of the section
        st.markdown(
            "<h3 style='text-align: center; color: #00BFFF;'>Volume and Price analyse</h3>",
            unsafe_allow_html=True,
        )

        # This month
        st.markdown(
            "<h5 style='color: #00BFFF;'>Actual month</h5>", unsafe_allow_html=True
        )
        month_trend = price_and_volume_kpi(
            df=today_analyse_price_data,
            col_price="this_month_trend",
            col_volume="this_month_volume",
            background_color=streamlit_background_color,
        )
        st.plotly_chart(month_trend, se_container_width=False, key="month_trend")

        # Last Month
        st.markdown(
            "<h5 style='color: #00BFFF;'>Last month</h5>", unsafe_allow_html=True
        )
        last_month_trend = price_and_volume_kpi(
            df=today_analyse_price_data,
            col_price="last_month_trend",
            col_volume="last_month_volume",
            background_color=streamlit_background_color,
        )
        st.plotly_chart(
            last_month_trend, use_container_width=False, key="last_month_trend"
        )

        # Year to date
        st.markdown(
            "<h5 style='color: #00BFFF;'>Year to date</h5>", unsafe_allow_html=True
        )
        year_to_date = price_and_volume_kpi(
            df=today_analyse_price_data,
            col_price="year_to_date_trend",
            col_volume="year_to_date_volume",
            background_color=streamlit_background_color,
        )
        st.plotly_chart(year_to_date, use_container_width=False, key="year_to_date")

        # One year rolling
        st.markdown(
            "<h5 style='color: #00BFFF;'>One year rolling</h5>", unsafe_allow_html=True
        )
        one_year_rolling = price_and_volume_kpi(
            df=today_analyse_price_data,
            col_price="one_year_rolling_trend",
            col_volume="one_year_rolling_volume",
            background_color=streamlit_background_color,
        )
        st.plotly_chart(
            one_year_rolling, use_container_width=False, key="one_year_rolling"
        )

        # # Year to date
        st.markdown(
            "<h5 style='color: #00BFFF;'>Five year rolling</h5>", unsafe_allow_html=True
        )
        five_year_rolling = price_and_volume_kpi(
            df=today_analyse_price_data,
            col_price="five_year_rollingtrend",
            col_volume="five_year_rolling_volume",
            background_color=streamlit_background_color,
        )
        st.plotly_chart(
            five_year_rolling, use_container_width=False, key="five_year_rolling"
        )

    with col[1]:
        st.markdown(
            "<h3 style='text-align: center; color: #FFD700;'>Historic stock</h3>",
            unsafe_allow_html=True,
        )
        five_year_historic_stock_data = pd.read_json(
            StringIO(json_data["historical_stock_info"]["5y_historic"])
        )

        # first graph
        candle_data = historic_stock_candle_stick_chart(
            df=five_year_historic_stock_data, height=250, width=600
        )
        st.plotly_chart(candle_data, use_container_width=False, key="candle_data")

        # second graph
        trend_graph = get_trends_events_graph(
            df=five_year_historic_stock_data,
            cols=["Open", "High", "Low", "Close"],
            degre=3,
            show_curve=True,
            colors={
                "Open": "cornflowerblue",
                "High": "forestgreen",
                "Low": "firebrick",
                "Close": "dimgrey",
            },
            height=400, width=600
        )
        st.plotly_chart(trend_graph, use_container_width=False, key="trend_graph")

    with col[2]:
        st.markdown(
            "<h3 style='text-align: center; color: #8338ec;'>Recommendation analyst</h3>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h3 style='text-align: center; color: #8338ec;'>Info about option</h3>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h3 style='text-align: center; color: #8338ec;'>Prediction</h3>",
            unsafe_allow_html=True,
        )
