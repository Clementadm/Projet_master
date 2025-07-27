import streamlit as st
from PIL import Image


def page_config(initial_sidebar_state="expanded"):
    im = Image.open("SRC/ihm/favicon/candlestick-chart.png")

    st.set_page_config(
        page_title="TradeHelper", layout="wide", page_icon=im,
        initial_sidebar_state=initial_sidebar_state)
    st.title("Bienvenue sur la plateforme IA Bourse 📈🤖")