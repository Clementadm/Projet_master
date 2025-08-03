import streamlit as st
from PIL import Image


def page_config(initial_sidebar_state="expanded", layout="wide"):
    # im = Image.open("SRC/ihm/favicon/candlestick-chart.png")
    logo = Image.open("SRC/ihm/favicon/logo.png")
    st.logo(logo, icon_image=logo, size="large")

    st.set_page_config(
        page_title="TradeHelper", layout=layout, page_icon=logo,
        initial_sidebar_state=initial_sidebar_state)
    st.sidebar.image(logo, width=300)
    # st.title("TradeHelper: Turning GOALS into GAINS")

    st.markdown("<h1 style='text-align: center; color: #ff5e34;'>TradeHelper</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #eddf98;'>Your AI-powered investment decision assistant</h4>", unsafe_allow_html=True)
    st.markdown("---")


def footer():
    st.html("""
        <div style='center; font-family: Roboto, sans-serif; color: #f0f2f5;'>
            <hr style='margin-top: 50px; margin-bottom: 20px; border: 1px solid #333;'>
            <p style='font-size: 13px; color: grey;'>© 2025 TradeHelper - Make faster, smarter investment decisions</p>
        </div>
    """)
