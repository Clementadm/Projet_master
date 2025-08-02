# # import streamlit as st
# # from PIL import Image
# # from ihm.set_page_config import page_config

# # page_config()


# # # st.markdown("""
# # # Ce site vous permet de :
# # # - 📊 Visualiser les principaux indicateurs financiers via un tableau de bord interactif
# # # - 📰 Suivre les dernières actualités du marché
# # # - 🤖 Explorer les prédictions générées par notre IA spécialisée

# # # Naviguez via le menu à gauche.
# # # """)

# # st.html(
# #     "<h1>Our solution</h>"
# # )

# # st.markdown(
# #     """
# # ## Our solution : 

# # #### Purpose
# # TradeHelper aims to provide an automated investment decision support tool, using financial, stock market, and news data to 
# # evaluate investment opportunities in publicly traded companies. 
# # It integrates both descriptive analysis (data, trends, indicators) and predictive analysis 
# # (machine learning model) to help you make the best possible investment decisions.

# # ### Key features
# # 1. Automatic retrieval of data from various sources
# # a) What
# # - Financial data on a company
# # - Stock market history,
# # - options,
# # - and economic and country news about the company
# # b)    How
# # Collected via APIs and web scraping, 
# # c) When 
# # orchestrated daily.
# # 2. Data processing and transformation
# # a) done by who ? 
# # Our data scientists specialize in data analysis are supported by financial experts and industry experts.
# # b) What did they do? 
# # They cleaned and processed the data to ensure that it was clean and consistent across all data sources. This made it possible to create clear, accurate, and simplified indicators from our data so that you can easily understand the data.
# # 3. machine learning section to predicted price tendance 
# # a) Automated prediction of the relevance of an investment 
# # b) Training and validation data stored to enable iteration and continuous improvement.
# # 4. interactive dashboard
# # creation of an interactive dashboard with several sections providing access to graphs and key indicators

# # ### User benefits
# # - Easy access to strategic information.
# # - Clear visualization of trends and analysis indicators.
# # - Immediate decision support thanks to automatic recommendations.
# # - Time savings through centralized and automated data processing.
# # - Smooth and intuitive experience, even for non-expert users.
# # """)

# # logo = Image.open("SRC/ihm/favicon/logo.png")
# # st.image(
# #     logo,
# #     caption="Logo"
# # )
# # # st.image(
# # #     "https://images.unsplash.com/photo-1480944657103-7fed22359e1d?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
# # #     caption="Analyse de données et visualisation")

# # ___________________________________________________________________________________________________
# # st.markdown("---")
# import streamlit as st
# from PIL import Image
# from ihm.set_page_config import page_config

# page_config()


# # 🎯 Purpose
# st.markdown("<h2 style='color: #ffde00;'>💡Purpose</h2>", unsafe_allow_html=True)
# st.markdown("""
# TradeHelper is an intelligent assistant designed to help you make better investment decisions using a mix of:
# - Financial and stock data
# - Country and company news 
# - Predictive analytics powered by Machine Learning

# Our goal is to help you : **identify and evaluate investment opportunities** in listed companies, simply and reliably.
# """)

# # 🛠️ Key Features
# st.markdown("## 🛠️ Key Features")

# st.markdown("### 1. 🔄 Automated Data Collection")
# st.markdown("""
# - **What**: Company fundamentals, market history, option contracts, and economic news.
# - **How**: Daily collection via APIs (e.g., Finnhub, NewsAPI) and scraping.
# - **When**: Automated every morning before the stock market opens.
# """)

# st.markdown("### 2. 🧹 Data Processing & Transformation")
# st.markdown("""
# - **By whom**: Data scientists and finance experts.
# - **Why**: To clean, normalize, and enrich data across all sources.
# - **What**: Generation of clear and reliable indicators (trend, sentiment, volumes...).
# """)

# st.markdown("### 3. 🤖 Predictive Modeling")
# st.markdown("""
# - **What**: Machine Learning model trained to predict market sentiment and investment relevance.
# - **How**: With traceable, versioned training/validation datasets.
# - **Why**: To give investment suggestions backed by historical patterns.
# """)

# st.markdown("### 4. 📊 Interactive Dashboard")
# st.markdown("""
# Explore your data visually:
# - Real-time trends
# - Financial KPIs
# - Analyst recommendations
# - Company news with sentiment
# """)

# # 🎁 User Benefits
# st.markdown("## 🎁 User Benefits")
# st.markdown("""
# - ✅ Quick access to essential investment signals.
# - 📉 Visual and intuitive trend interpretation.
# - 🚀 Instant insight thanks to automated predictions.
# - 🧠 Smart assistance for non-experts.
# - ⏳ Save time via centralized intelligence.
# """)

# # 🎯 Footer
# st.markdown("---")
# st.markdown("<p style='text-align: center; font-size: 13px; color: grey;'>© 2025 TradeHelper - Your investment intelligence companion</p>", unsafe_allow_html=True)

# ___________________________________________________________________________________________________
# st.markdown("---")
import streamlit as st
from PIL import Image
from ihm.set_page_config import page_config

page_config()

st.html("""
    <div style='text-align: center; padding: 10px 50px; font-family: Roboto, sans-serif;'>
        <h2 style='color: #ffde00;'>💡 Purpose</h2>
    </div>
""")
st.html("""
    <div style='center; font-family: Roboto, sans-serif; color: #f0f2f5;'>
        <p style='font-size: 16px; max-width: 800px; margin: auto;'>
            <strong>TradeHelper</strong> is an intelligent assistant designed to help you make better investment decisions using a mix of:</p>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    •🏦 Financial and stock data</pre>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    •📰 Country and company news</pre>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    •⚙️ Predictive analytics powered by Machine Learning</pre>
        <p style='font-size: 16px; max-width: 800px; margin: auto;'>
            Our goal is to help you <strong>identify and evaluate investment opportunities</strong> in listed companies, simply and reliably.
        </p>
    </div><br><br>
    
""")

st.html("""
    <div style='text-align: center; padding: 10px 50px; font-family: Roboto, sans-serif;'>
        <h2 style='color: #ffde00;'>🎛️ Key Features</h2>
    </div>
""")
st.html("""
    <div style='center; font-family: Roboto, sans-serif; color: #f0f2f5;'>
        <h3 style='max-width: 800px; margin: auto;'>1. 🔄 Automated Data Collection</h3>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    •<strong> What</strong>: Company fundamentals, market history, option contracts, and economic news. </pre>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    •<strong> How</strong>: Daily collection via APIs (e.g., Finnhub, NewsAPI) and scraping.</pre>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    •<strong> When</strong>: Automated every morning before the stock market opens.</pre>
        <br>

        <h3 style='max-width: 800px; margin: auto;'>2. 🧹 Data Processing & Transformation</h3>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    •<strong> By whom</strong>: Data scientists and finance experts. </pre>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    •<<strong> Why</strong>: To clean, normalize, and enrich data across all sources. </pre>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    •<strong> What</strong>: Generation of clear and reliable indicators (trend, sentiment, volumes...). </pre>
        <br>

        <h3 style='max-width: 800px; margin: auto;'>3. ⚙️ Predictive Modeling</h3>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    •<strong> What</strong>: ML model to predict market sentiment and investment relevance </pre>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    •<strong> How</strong>: With traceable, versioned training/validation datasets </pre>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    •<strong> Why</strong>: To give suggestions backed by historical patterns. </pre>
        <br>

        <h3 style='max-width: 800px; margin: auto;'>4. 📊 Interactive Dashboard</h3>
        <p style='font-size: 16px; max-width: 800px; margin: auto;'>Explore your data visually:</p>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    • Real-time trends</pre>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    • Financial KPIs </pre>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    • Analyst recommendations </pre>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    • Company and country news with  analysis sentiment </pre>
        
    </div><br><br>
""")

st.html("""
    <div style='text-align: center; padding: 10px 50px; font-family: Roboto, sans-serif;'>
        <h2 style='color: #ffde00;'>.☘︎ ݁˖ User Benefits</h2>
    </div>
""")
st.html("""
    <div style='center; font-family: Roboto, sans-serif; color: #f0f2f5;'>

        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    •🚀 Quick access to essential investment signals.</pre>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    •👁️ Visual and intuitive trend interpretation.</pre>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    •🔎 Instant insight thanks to automated predictions.</pre>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    •⏳ Save time via centralized intelligence.</pre>

    </div><br><br>
""")


st.html("""
    <div style='center; font-family: Roboto, sans-serif; color: #f0f2f5;'>
        <hr style='margin-top: 50px; margin-bottom: 20px; border: 1px solid #333;'>
        <p style='font-size: 13px; color: grey;'>© 2025 TradeHelper - Your investment intelligence companion</p>
    </div>
""")
