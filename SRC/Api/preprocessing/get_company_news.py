# %%
from datetime import datetime, timedelta
from API.get_data.api_finnhub import get_company_news
from API.get_data.api_apinews_org import get_news
import pandas as pd


# %%
def finnhub_data(business_name):
    """
    Get news from finnhub api for the business ticker enter.
    We retrieve news from the last 7 days
    Can only be use for American companies
    """
    # News from the last 7 days
    from_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    today = datetime.now().strftime("%Y-%m-%d")

    finnhub_news = get_company_news(business_name, from_date, today)
    finnhub_news = finnhub_news[
        [
            "year",
            "month",
            "day",
            "datetime",
            "headline",
            "summary",
            "source",
            "url",
            "id",
        ]
    ]
    finnhub_news.columns = [
        "year",
        "month",
        "day",
        "publishedAt",
        "headline",
        "summary",
        "source",
        "url",
        "id",
    ]
    finnhub_news["API"] = "finnhub_news"
    print("News recover from finhub")
    return finnhub_news


# f_n = finnhub_data("TSLA")


# %%
def apinewsorg_data(business_name):
    """
    Get all the news from api_news_org api who contains the business name in the article
    We retrieve news from the last 15 days
    /!\ some of the news may have no connection with the company if just mentioned in the article
    """
    api_news_org = get_news(business_name=business_name, anteriorite_en_jours=14)
    api_news_org["publishedAt"] = api_news_org["publishedAt"].apply(lambda x: x[:10])
    api_news_org["publishedAt"] = pd.to_datetime(api_news_org["publishedAt"])
    api_news_org["year"] = api_news_org["publishedAt"].apply(lambda x: x.year)
    api_news_org["month"] = api_news_org["publishedAt"].apply(lambda x: x.month)
    api_news_org["day"] = api_news_org["publishedAt"].apply(lambda x: x.day)
    api_news_org = api_news_org[
        [
            "year",
            "month",
            "day",
            "publishedAt",
            "title",
            "description",
            "source.name",
            "url",
        ]
    ]
    api_news_org.columns = [
        "year",
        "month",
        "day",
        "publishedAt",
        "headline",
        "summary",
        "source",
        "url",
    ]
    api_news_org["API"] = "api_news_org"
    print("News recover from api_news_org")
    return api_news_org


# apinewsorg_data("Tesla")


# %%
def create_news_dataset(business_name, business_ticker):
    """ "
    Call the two functions that collect the news from the API
    News processing to ensure consistency and similarity
    News are sorted in order of publication from most recent to oldest
    Save news in Data/Output
    """
    api_news_org = apinewsorg_data(business_name)
    finnhub_news = finnhub_data(business_ticker)
    # api_news_org = api_news_org.drop("url", axis=1)
    # finnhub_news = finnhub_news.drop(["url", "id"], axis=1)
    finnhub_news = finnhub_news.drop(["id"], axis=1)

    company_news = pd.concat([api_news_org, finnhub_news])
    company_news.sort_values("publishedAt", ascending=False, inplace=True)
    company_news.reset_index(inplace=True)
    company_news.to_csv(
        "../Data/Output/News/Company/"
        + datetime.now().strftime("%Y_%m_%d__%H_%M")
        + "__news_from_finhubb_and_apinewsorg.csv"
    )
    print("News processing done and save")
    return company_news


# create_news_dataset(business_name="Tesla", business_ticker="TSLA")
