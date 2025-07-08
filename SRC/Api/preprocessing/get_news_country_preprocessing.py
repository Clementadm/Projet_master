# %%
from API.get_data.api_finnhub import get_general_news_country
from utils.llm_call import create_prompt_company_news, get_news_sentiment


# %%
def get_news_country():
    finnhub_country_news = get_general_news_country()
    finnhub_country_news = finnhub_country_news[
        ["publishedAt", "year", "month", "day", "headline", "summary", "source", "url"]
    ]
    # finnhub_country_news.rename(columns={"datetime": "publishedAt"}, inplace=True)
    # return finnhub_country_news
    finnhub_country_news["prompt"] = finnhub_country_news.apply(create_prompt_company_news, axis=1)
    finnhub_country_news["sentiment"] = finnhub_country_news["prompt"].apply(get_news_sentiment)
    print("Country news processing done")
    return finnhub_country_news.to_json()


# %%
# a = get_news_country()
# a
