# %%
import requests

# from get_api_keys import API_KEY_FINNHUB
from .get_api_keys import API_KEY_FINNHUB
from datetime import datetime, timedelta
import os
import pandas as pd
import json
import finnhub

# %% [markdown]
# # <h1 style="color:red"> API FINHUB

# %%
finnhub_client = finnhub.Client(api_key=API_KEY_FINNHUB)

# %% [markdown]
# ## <h2 style="color:purple"> NEWS

# %% [markdown]
# ### <h3 style="color:cyan"> get_company_news


# %%
def get_company_news(business_name, begin_date, end_date):
    news = finnhub_client.company_news(business_name, _from=begin_date, to=end_date)
    news = pd.json_normalize(news)
    news["datetime"] = news["datetime"].apply(lambda x: datetime.fromtimestamp(x))
    news["year"] = news["datetime"].apply(lambda x: x.year)
    news["month"] = news["datetime"].apply(lambda x: x.month)
    news["day"] = news["datetime"].apply(lambda x: x.day)
    print(
        f"News sur {news.loc[0, "datetime"] - news.loc[len(news)-1, "datetime"]} jours "
    )
    return news


# %%
# from_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
# today = datetime.now().strftime("%Y-%m-%d")

# # a = get_company_news('TSLA', "2024-01-01", "2024-11-01")
# finnhub_business_news = get_company_news("TSLA", from_date, today)

# # %%
# finnhub_business_news.shape

# # %%
# finnhub_business_news.head(3)

# %% [markdown]
# ### <h3 style="color:cyan"> get_general_news_country


# %%
def get_general_news_country():
    news = pd.json_normalize(
        finnhub_client.general_news(
            "general"
        )  # Accès aux dernières nouvelles générales, de forex, de crypto, et de fusions.
    )
    news["datetime"] = news["datetime"].apply(lambda x: datetime.fromtimestamp(x))
    news["year"] = news["datetime"].apply(lambda x: x.year)
    news["month"] = news["datetime"].apply(lambda x: x.month)
    news["day"] = news["datetime"].apply(lambda x: x.day)
    print(
        f"News sur {news.loc[0, "datetime"] - news.loc[len(news)-1, "datetime"]} jours "
    )
    return news


# %%
# finnhub_country_news = get_general_news_country()

# # %%
# finnhub_country_news.shape

# # %%
# finnhub_country_news.head(3)

# %% [markdown]
# ## <h2 style="color:purple"> Financial information about the company

# %% [markdown]
# ### <h3 style="color:cyan"> Competitor


# %%
def get_competitor(business_name):
    """get concurent"""
    company_peers = finnhub_client.company_peers(business_name)
    return company_peers


# %%
# get_competitor("AAPL")

# %% [markdown]
# ### <h3 style="color:cyan"> Recommendation trends


# %%
def recommendation_trends(business_name):
    # Recommendation trends Recommandations des analystes, cibles de prix et surprises sur les bénéfices.
    recommendation = pd.json_normalize(
        finnhub_client.recommendation_trends(business_name)
    )
    return recommendation


# %%
# recommendation_trends("AAPL")

# %% [markdown]
# ### <h3 style="color:cyan"> Insider sentiment


# %%
def insider_sentiment(business_name, begin_date, end_date):
    """
    sentiment des initiés (dirigeants d'entreprises) concernant des sociétés américaines. Cette mesure est calculée en utilisant la méthode MSPR (Mean Sentiment Per Report),
    qui évalue le sentiment global exprimé dans les rapports d'insiders.
    L'échelle de MSPR va de -100 (très négatif) à 100 (très positif)
    Ces sentiments peuvent être utilisés pour anticiper des changements de prix dans les 30 à 90 jours à venir.
    """
    df = pd.json_normalize(
        finnhub_client.stock_insider_sentiment(business_name, begin_date, end_date)[
            "data"
        ]
    )
    return df


# %%
# insider_sentiment("AAPL", from_date, today)

# %% [markdown]
# ### <h3 style="color:cyan"> Info businness


# %%
def info_company(business_name):
    df = pd.json_normalize(finnhub_client.company_profile2(symbol=business_name))
    df = df[["country", "currency", "finnhubIndustry", "marketCapitalization"]]
    return df


# %%
# info_company("AAPL")
