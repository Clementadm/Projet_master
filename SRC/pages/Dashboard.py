import streamlit as st
import pandas as pd
from io import StringIO
from ihm.set_page_config import page_config
from ihm.utils.read_json_file import read_json_file
from pages.subfolder_dashboard.financial_dashboard import financial_dashboard
from pages.subfolder_dashboard.company_news_dashboard import company_news
from ihm.utils.get_data_from_choosen_company import get_data_of_choosen_company

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
    today_analyse_price_data = pd.read_json(
        StringIO(json_data["historical_stock_info"]["today_analyse_price"])
    )
    finance_tab, company_news_tab, country_news_tab = st.tabs(
        ["Financial Dashboard", "Company news", "Country News"]
    )
    with finance_tab:
        financial_dashboard(
            json_data=json_data,
            today_analyse_price_data=today_analyse_price_data,
            streamlit_background_color=streamlit_background_color,
        )

    with company_news_tab:
        company_news(json_data, "company_news")

    with country_news_tab:
        company_news(json_data, "country_news")
