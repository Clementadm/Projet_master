import streamlit as st
from ihm.set_page_config import page_config, footer

page_config(initial_sidebar_state="collapsed", layout="centered")

# glossaire expliquant les termes techniques
# Comment fonctionne la solution ?”,
# “D’où proviennent les données utilisées dans le dashboard ?”,
# ou encore “À quelle fréquence les données sont-elles mises à jour ?”.
# Quelle est le prix de la solution
# Qui a réalisé la solution
# Dou viennet données
# interprétation des visualisations graphiques,
# lecture et l'explicabilité des prédictions de notre algorithme,
# l'intégration de toutes ces informations dans un processus de décision d'investissement personnel et réfléchi.

# Understand the solution
st.html("""
    <div style='text-align: center; font-family: Roboto, sans-serif;'>
        <h2 style='color: #ffde00;'>Understand the solution</h2>
    </div>
""")
with st.expander(" What is TradeHelper"):
    st.write("""
        TradeHelper is an intelligent assistant designed to help you make better investment decisions.
        Our goal is to help you identify and evaluate investment opportunities in listed companies, simply and reliably.
    """)

with st.expander("Is the solution free or paid?"):
    st.write("""
        The solution is currently free as it is under development and evaluation.
        Future versions may include a freemium model, offering free access to basic features and premium plans for advanced 
        analytics, API access, and integration features.
    """)

with st.expander("Who developed TradeHelper ?"):
    st.write("""
        This solution was developed by a team of data scientists and developers specializing in finance and artificial 
        intelligence, as part of an academic and professional innovation project.
    """)

with st.expander("How does TradeHelper work as a whole?"):
    st.write("""
        The platform automatically collects financial, market, and news data from various sources (APIs and scraping).
        It then processes and standardizes the data before feeding it into a machine learning model trained to detect 
        market sentiment and assess investment opportunities. The results are visualized through an interactive dashboard 
        built with Streamlit and Plotly.
    """)
st.markdown("---")

# Data used
st.html("""
    <div style='text-align: center; font-family: Roboto, sans-serif;'>
        <h2 style='color: #ffde00;'>Data used</h2>
    </div>
""")
with st.expander("Where does the data displayed on the dashboard come from?"):
    st.write("""
        We use trusted data providers, including Finnhub, NewsAPI and Yahoo Finance.
        They provide us with financial data, historical stock prices, analyst recommendations and relevant 
        news articles, which we then process to create KPIs.
    """)

with st.expander("How frequently is the data updated?"):
    st.write("""
        The data is collected and updated on a daily basis, usually in the evening (timezone→Paris), ensuring that the most recent data is reflected 
        at the end of the previous day.
    """)

with st.expander("How is the reliability of the data ensured?"):
    st.write("""
        We rely on reputable sources and carry out checks during the pre-processing of data.
        Duplicates, missing values, and outliers are handled carefully. 
        To improve consistency and reliability, we also cross-reference multiple data sources.
    """)
st.markdown("---")

# Interpretation of Results
st.html("""
    <div style='text-align: center; font-family: Roboto, sans-serif;'>
        <h2 style='color: #ffde00;'>Interpretation of Results</h2>
    </div>
""")
with st.expander("How should the graphs be interpreted?"):
    st.write("""
        Each graph provides a visual representation of price trends, trading volumes, analyst sentiment and stock evolution.
        The colours and arrows (e.g. '⬆ Bullish' and '⬇ Bearish') help you to interpret the data at a glance.
    """)

with st.expander("What is the correct interpretation of the predictions made by the algorithm?"):
    st.write("""
        Predictions are machine learning-based estimates of price direction or investment relevance.
        They should be used to support decisions, not as the only factor.
    """)

with st.expander("What are the main indicators used in the analysis?"):
    st.markdown("""
        We use:  
            - Technical indicators (trend, volatility, volume),  
            - Analyst recommendations (buy, hold, sell),  
            - Market sentiment analysis (from news),  
            - Price targets and spread ratios from option data.  
    """)
with st.expander("What is the margin of uncertainty or limitation of predictions?"):
    st.write("""
        As with any predictive model, the results are probabilistic and subject to uncertainty.
        market may be influenced in unexpected ways by external factors such as breaking news and geopolitical events. 
        The model is updated regularly to adapt to market shifts.
    """)
st.markdown("---")

# Decision-Making
st.html("""
    <div style='text-align: center; font-family: Roboto, sans-serif;'>
        <h2 style='color: #ffde00;'>Decision-Making</h2>
    </div>
""")
with st.expander("What is the best way to combine different types of information when making investment decisions?"):
    st.write("""
        The dashboard brings together a variety of indicators, enabling users to compare multiple perspectives, such as historical trends, 
        analyst opinions, sentiment scores and algorithmic predictions, all in one place, to help them make informed decisions.
    """)
with st.expander("How can this solution help me invest more wisely?"):
    st.write("""
        TradeHelper saves time by revealing key insights that might otherwise be overlooked.
It combines technical, sentiment and predictive indicators to enable non-experts to assess the market more effectively.
    """)
with st.expander("What is the system's approach to user risk level or objectives?"):
    st.write("""
        In the current version, the same predictions are shown to all users. 
        However, a future update may allow customisation according to risk tolerance or investment goals.
    """)

footer()