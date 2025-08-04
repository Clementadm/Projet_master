import streamlit as st
from ihm.graph.analyse_price_of_the_day import price_and_volume_kpi
import pandas as pd
from io import StringIO
from ihm.graph.options import (
    graph_comparate_actual_price_with_option_price,
    bar_chart_options,
)

from ihm.graph.analyst_recommendation import (
    analyst_price_recommendation,
    breakdown_of_sentiment_analyst,
)

# from datetime import datetime
from ihm.graph.historical_stock_data import (
    historic_stock_candle_stick_chart,
    get_trends_events_graph,
)


def financial_dashboard(
    json_data, today_analyse_price_data, streamlit_background_color
):
    col = st.columns((2.5, 4, 2.5), gap="medium")  # , vertical_alignment="center")
    # _______________________________________________________________________
    with col[0]:
        # title of the section
        st.markdown(
            "<h3 style='text-align: center; color: #04d995;text-decoration: underline'>Analyst recommendation</h3>",
            unsafe_allow_html=True,
        )
        # graph title
        st.markdown(
            "<h5 style='color: #04d995;'>Analyst sentiment distribution</h5>",
            unsafe_allow_html=True,
        )

        sentiment_of_the_analyst = breakdown_of_sentiment_analyst(
            positive_sentiment=json_data["historical_stock_info"][
                "breakdown_of_analyst_recommendation"
            ]["distribution_of_recommendations"]["positif"],
            negative_sentiment=json_data["historical_stock_info"][
                "breakdown_of_analyst_recommendation"
            ]["distribution_of_recommendations"]["negatifs"],
            # json_data["historical_stock_info"]["breakdown_of_analyst_recommendation"][
            #     "distribution_of_recommendations"
            # ]
        )

        st.plotly_chart(
            sentiment_of_the_analyst,
            use_container_width=False,
            key="sentiment_of_the_analyst",
        )

        # title of the section
        st.markdown(
            "<h3 style='text-align: center; color: #00BFFF;text-decoration: underline'>Volume and Price analyse</h3>",
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

    # _______________________________________________________________________
    with col[1]:
        st.markdown(
            "<h3 style='text-align: center; color: #FFD700;text-decoration: underline'>Historic stock</h3>",
            unsafe_allow_html=True,
        )
        col_last_price = st.columns((4, 4), gap="large")
        with col_last_price[0]:
            # open
            last_open_price_know = today_analyse_price_data["Open"].values[0]
            st.badge(f"Last open price: {last_open_price_know:.3f} $", icon=":material/check:", color="green", width="stretch")

            # close
            last_close_price_know = today_analyse_price_data["Close"].values[0]
            st.badge(f"Last close price: {last_close_price_know:.3f} $", icon=":material/close:", color="red", width="stretch")

        with col_last_price[1]:
            # low
            last_low_price_know = today_analyse_price_data["Low"].values[0]
            st.badge(f"Last low price: {last_low_price_know:.3f} $", icon=":material/arrow_downward:", color="red", width="stretch")

            # up
            last_up_price_know = today_analyse_price_data["High"].values[0]
            st.badge(f"Last low price: {last_up_price_know:.3f} $", icon=":material/arrow_upward:", color="green", width="stretch")

        # _________________
        # tendance sur 6 mois plus que 5 ans plus approprié
        # _________________
        # ou dérivé seconde ==> permetta de savpir quand commence a ne plus augmenter aussi vite qu'avant
        #
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
            height=400,
            width=600,
        )
        st.plotly_chart(trend_graph, use_container_width=False, key="trend_graph")

    # _______________________________________________________________________
    with col[2]:
        # OPTIONS
        # _______________________________________________________________________
        st.markdown(
            "<h3 style='text-align: center; color: #8338ec;text-decoration: underline'>Info about currently active options</h3>",
            unsafe_allow_html=True,
        )

        # graph title
        st.markdown(
            "<h5 style='color: #8338ec;'>Actual price VS Analyst price</h5>",
            unsafe_allow_html=True,
        )
        # Options price recommendation
        option_price = analyst_price_recommendation(
            json_data["options"], background_color=streamlit_background_color
        )
        st.plotly_chart(
            option_price,
            use_container_width=False,
            key="option_price",
        )
        st.write("---")
        # indicator
        options_price_comparative = graph_comparate_actual_price_with_option_price(
            cluster_buy=json_data["options"]["cluster_buy"][0],
            cluster_sell=json_data["options"]["cluster_sell"][0],
            background_color=streamlit_background_color,
        )
        st.plotly_chart(
            options_price_comparative,
            use_container_width=False,
            key="options_price_comparative",
        )

        # graph en bar
        # graph title
        st.markdown(
            "<h5 style='color: #8338ec;'>Mean Buy/Sell options Comparison</h5>",
            unsafe_allow_html=True,
        )
        bar_options = bar_chart_options(
            background_color=streamlit_background_color,
            # left
            left_bar_y_buy=json_data["options"]["buy_mean_volume"],
            left_bar_y_sell=json_data["options"]["sell_mean_volume"],
            left_title="Mean options volume",
            left_yaxis_title="Mean  volume",
            # right
            right_bar_y_buy=json_data["options"]["nb_option_buy"],
            right_bar_y_sell=json_data["options"]["nb_option_sell"],
            right_title="Number  of  different  options",
            right_yaxis_title="Number of options",
        )
        st.plotly_chart(
            bar_options,
            use_container_width=False,
            key="bar_options",
        )

        st.markdown(
            "<h3 style='text-align: center; color: #8338ec;text-decoration: underline'>Prediction</h3>",
            unsafe_allow_html=True,
        )
