# %%
from datetime import datetime, timedelta
from API.get_data.api_finnhub import get_general_news_country
import pandas as pd

# %%
def get_news_country():
    finnhub_country_news = get_general_news_country()
    finnhub_country_news = finnhub_country_news[['year', 'month', 'day', 'headline', 'summary', 'source', 'url']]
    # return finnhub_country_news
    return finnhub_country_news.to_json()

# %%
# a = get_news_country()
# a
