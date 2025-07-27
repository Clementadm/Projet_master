import streamlit as st
import pandas as pd
import plotly.express as px
from ihm.set_page_config import page_config

page_config()


st.markdown("""
Ce site vous permet de :
- 📊 Visualiser les principaux indicateurs financiers via un tableau de bord interactif
- 📰 Suivre les dernières actualités du marché
- 🤖 Explorer les prédictions générées par notre IA spécialisée

Naviguez via le menu à gauche.
""")

st.image(
    "https://images.unsplash.com/photo-1480944657103-7fed22359e1d?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
    caption="Analyse de données et visualisation")

st.markdown("---")