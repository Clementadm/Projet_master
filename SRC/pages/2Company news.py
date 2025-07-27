import streamlit as st
import pandas as pd
from io import StringIO
from ihm.set_page_config import page_config
from ihm.utils.get_data_from_choosen_company import get_data_of_choosen_company
from ihm.utils.read_json_file import read_json_file
from ihm.graph.news_table import get_news
import io

page_config(initial_sidebar_state="collapsed")
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
    st.markdown(
        "<h3 style='text-align: center; color: #04d995;text-decoration: underline'>Company News & Sentiment Analysis</h3>",
        unsafe_allow_html=True,
    )
    company_news = get_news(
        json_data["news"]["company_news"],
    )
    
    st.data_editor(
        company_news,
        column_config={
            "url": st.column_config.LinkColumn("url"),
            **{col: st.column_config.Column(width="small") for col in company_news.columns if col != "url"}
        },
        hide_index=True,
        height=800,
        num_rows="fixed",
        use_container_width=True
    )