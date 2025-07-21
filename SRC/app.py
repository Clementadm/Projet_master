import streamlit as st
import pandas as pd
# import altair as alt
import plotly.express as px


st.set_page_config(
    page_title="Projet IA Bourse", layout="wide", page_icon="📊",
    initial_sidebar_state="expanded")
st.title("Bienvenue sur la plateforme IA Bourse 📈🤖")

# df=pd.read_csv(r"C:\Users\cleme\Documents\Ynov\M2\Projet Master\Projet Bourse\NEW\Projet_master\SRC\us-population-2010-2019.csv")
# df_reshaped = pd.melt(df, id_vars=['states', 'id'], var_name='year', value_name='population')
# # Convert 'year' column values to integers
# df_reshaped['states'] = df_reshaped['states'].astype(str)
# df_reshaped['year'] = df_reshaped['year'].astype(int)
# df_reshaped['population'] = df_reshaped['population'].str.replace(',', '').astype(int)

# with st.sidebar:
#     st.title('🏂 US Population Dashboard')
    
#     year_list = list(df_reshaped.year.unique())[::-1]
    
#     selected_year = st.selectbox('Select a year', year_list, index=len(year_list)-1)
#     df_selected_year = df_reshaped[df_reshaped.year == selected_year]
#     df_selected_year_sorted = df_selected_year.sort_values(by="population", ascending=False)

#     color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
#     selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

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