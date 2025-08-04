import streamlit as st
from ihm.set_page_config import page_config, footer

page_config(initial_sidebar_state="collapsed", layout="centered")

st.html("""
    <div style='text-align: center; font-family: Roboto, sans-serif;'>
        <h2 style='color: #ffde00;'>🎓 Tutorial – How to Use TradeHelper</h2>
    </div>
""")

st.html("""
    <div style='center; font-family: Roboto, sans-serif; color: #f0f2f5;'>
        <p style='font-size: 16px; max-width: 800px; margin: auto;'>
            This section will help you to get started quickly and explore all of the platform's key features with ease.
            Whether you're a beginner or an experienced user, we will walks you through the entire solution
            You’ll also find external learning resources about finance, stock markets, and investment strategies to deepen your knowledge and make more informed decisions.
            The goal: Make you autonomous and confident in using the platform for your investment analysis.
        </p>
    </div><br><br>
""")
st.warning("""
    &nbsp; &nbsp; DISCLAIMER \n
    It is important to note that past performance does not guarantee future results.  
    TradeHelper is a decision support tool, it should not be considered a financial advisor.  
    It is imperative to combine model outputs with your own judgment and to consult professionals when necessary.  
    """, icon="⚠️")

with st.expander("How to naviguate between pages ?"):
    st.write("""
        TradeHelper is built with Streamlit multi-age support.
        To switch between pages (Dashboard, News, Tutorials, and so on), simply use the menu in the sidebar on the left.
        Each page is dedicated to a specific function.
    """)

with st.expander("How to filter the dashboard by company ? "):
    st.write("""
        At the top of the Dashboard page, you will find a dropdown menu that allows you to select a specific company (e.g. Tesla, Microsoft, etc.).
        Once selected, all the graphs and indicators on the page will update automatically based on your choice.
    """)

with st.expander("How can I expand an graph ?"):
    st.write("""
        To view a graph in full-screen mode, please click the small square icon → ⛶ (found in the top-right corner of the Plotly chart).
        This action opens the chart in a larger, interactive window.
    """)

with st.expander("Instructions on how to use Zoom, Pan and Filter"):
    st.markdown("""
         All charts constructed with Plotly provide the following tools: 
            - ✚ Zoom: To zoom in on an area, drag the cursor across it.
            - ✋ Pan: To navigate the chart, please use the hand icon.
            - 🏠︎ Reset: To return to the original view, please click on either "Autoscale" or "Reset axes".
            - 📷 Screenshot: To download the chart as a PNG file, please click the camera icon.
    """)

with st.expander("How to understanding all the graphs & indicators"):
    st.markdown("""
        Each chart is interactive and colour-coded for clarity. The following is a guide to interpreting the results:  
            - Price and Volume Indicators: Show current trend sentiment (e.g. “Bullish”, “Bearish”).
            - Prediction Kpi: Show the recommend behavior that our model predicted
            - Options Analysis: Assess current pricing and volume trends in the options market and an analysis of what does the expert think about the price
            - Candle Stick Chart: This is a professional tool that displays stock performance over time. It uses green and red candles to show price movement.  
        By hovering the cursor over a specific point, the precise value or date are displayed.  
    """)

with st.expander("How to understanding the country and company new dashboard and table ?"):
    st.markdown("""
        The News section shows recent headlines related to your selected company. It contains:
            - Date: When the article was published
            - Headline: The main title of the news item.
            - Summary: Brief content overview
            - Source: The publisher, for example, could be Bloomberg or Reuters.
            - Sentiment: This indicator is calculated by our fine-tune LLM to determine whether an article is considered positive or negative (green for positif and red for negatif)
            - URL: Clickable link to the full article
        This allows you rapid evaluation of public sentiment and relevant market events.  
    """)

with st.expander("How can I isolate one data series on a chart ?"):
    st.markdown("""
        You can hide and show specific data series by clicking on a legend label (e.g. "Buy volume"). 
        To hide all other labels, double-click the relevant one.
    """)

with st.expander("Why don’t I see all data points on a graph ?"):
    st.markdown("""
        Some graphs automatically aggregate or filter data in order to enhance clarity. 
        Please use zoom or hover to inspect specific points, and verify any filters applied.
    """)

with st.expander("Would it be possible to compare two time periods on a chart?"):
    st.markdown("""
        Yes, you can zoom into two different time frames and toggle between them using the zoom and pan tools in Plotly. 
        Alternatively, you can download the image and compare them side-by-side manually.
    """)

with st.expander("How can I select a specific date range in a graph ?"):
    st.markdown("""
        Please click and drag across the desired date range. 
        As an alternative option, you can use the "range slider" located below the graphs (if available) to adjust the period.
    """)

with st.expander("How can the exact value of a data point be determined ?"):
    st.markdown("""
        Hover your mouse over the chart. A tooltip will appear showing the exact value, date, and label of the selected point.
    """)

with st.expander("Can I interact with the data behind the graphs ?"):
    st.markdown("""
        While not directly applicable, graphs are interactive (zoom, filter, explore). 
        Full datasets will be available to download in a future release.
    """)

with st.expander("What if a graph doesn't display correctly ?"):
    st.markdown("""
        Try refreshing the page or clearing your browser cache. 
        If the issue persists, please contact support via the Contact page.
    """)

with st.expander("Can I view charts on my mobile ?"):
    st.markdown("""
        Yes, but the experience has been optimised for desktop. 
        Please note that on mobile, some interactive elements may be less fluid due to screen constraints.
    """)

st.html("""
    <br><br>
    <div style='text-align: center; font-family: Roboto, sans-serif;'>
        <h2 style='color: #ffde00;'>Want to Learn More About Finance?</h2>
    </div>
""")
st.write("""
    Please find below some external resources that will help to develop your financial knowledge.
    Those will provide a solid foundation in investment theory, risk management, and decision-making skills.
""")

st.markdown("""
        - [Coursera](https://www.coursera.org/courses?query=stock%20market)
        - [Investopedia](https://www.investopedia.com/learn-how-to-trade-the-market-in-5-steps-4692230)
        - [GENEVE University](https://www.unige.ch/formcont/en/courses/mooc-financial-markets)
        - [FLAME University](https://www.flame.edu.in/pdfs/fil/presentations/FIL_Stock%20Market.pdf)
    """)

footer()
