import streamlit as st
from ihm.set_page_config import page_config, footer

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
        <p style='font-size: 16px; max-width: 800px; margin: auto;'>
            Here you’ll find:
        </p>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    • An interactive dashboard to visualize your data</pre>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    • A section for news and sentiment related to your selected companies</pre>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    • A tutorial to guide you through all the features</pre>
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    • A FAQ and Contact page if you need help or want to share feedback</pre>
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
        <pre style='font-size: 16px; max-width: 800px; margin: auto;'>    •<strong> Why</strong>: To clean, normalize, and enrich data across all sources. </pre>
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


footer()