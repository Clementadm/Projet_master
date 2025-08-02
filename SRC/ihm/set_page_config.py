import streamlit as st
from PIL import Image


def page_config(initial_sidebar_state="expanded"):
    # im = Image.open("SRC/ihm/favicon/candlestick-chart.png")
    logo = Image.open("SRC/ihm/favicon/logo.png")
    st.logo(logo, icon_image=logo, size="large")

    st.set_page_config(
        page_title="TradeHelper", layout="wide", page_icon=logo,
        initial_sidebar_state=initial_sidebar_state)
    st.sidebar.image(logo, width=300)
    # st.title("TradeHelper: Turning GOALS into GAINS")

    st.markdown("<h1 style='text-align: center; color: #ff5e34;'>TradeHelper</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #eddf98;'>Your AI-powered investment decision assistant</h4>", unsafe_allow_html=True)
    st.markdown("---")