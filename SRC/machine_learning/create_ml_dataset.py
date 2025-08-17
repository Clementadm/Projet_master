# %%
import numpy as np
import pandas as pd
from io import StringIO
import os
import json
# %% [markdown]
# # constitution du nouveau dataset


# %%
def get_sentiment_from_news_dataset(news_type: str, df) -> tuple[str, str]:
    company_news = pd.read_json(StringIO(df["news"][news_type]))

    positif_sentiment = sum(
        company_news[company_news["sentiment"] == 1]["sentiment"].values
    )
    negatif_sentiment = len(
        company_news[company_news["sentiment"] == 0]["sentiment"].values
    )

    total_sentiment = positif_sentiment + negatif_sentiment

    positif_distribution_pourcentage = positif_sentiment / total_sentiment
    negatif_distribution_pourcentage = negatif_sentiment / total_sentiment
    return positif_distribution_pourcentage, negatif_distribution_pourcentage


# %%
def create_dataset_from_all_file() -> pd.DataFrame:
    """
    Parse each file that have all the data collect and clean for each day.
    Selct the data an regroup it in one dataframe
    """
    directory = r"C:\Users\cleme\Documents\Ynov\M2\Projet Master\Projet Bourse\NEW\Projet_master\data\output\all_data_regroup"
    machine_learning_dataset = {
        "company_name": [],
        "date_bourse": [],
        "open_price": [],
        "close_price": [],
        "low_price": [],
        "high_price": [],
        "finnhubIndustry": [],
        "mean_sell": [],
        "mean_strongBuy": [],
        "mean_strongSell": [],
        "insider_sentiment": [],
        "company_posit_dist_percet": [],
        "company_negat_dist_percet": [],
        "country_posit_dist_percet": [],
        "country_negat_dist_percet": [],
        "analyst_sentiment_distribution": [],
        "analyst_price_target": [],
        "volume_action": [],
        "this_month_most_direction": [],
        "last_month_most_direction": [],
        "year_to_date_direction": [],
        "one_year_rolling_period_most_direction": [],
        "five_year_rolling_period_most_direction": [],
        "this_month_trend": [],
        "last_month_trend": [],
        "year_to_date_trend": [],
        "one_year_rolling_trend": [],
        "five_year_rollingtrend": [],
        "this_month_volume": [],
        "last_month_volume": [],
        "year_to_date_volume": [],
        "one_year_rolling_volume": [],
        "five_year_rolling_volume": [],
        "analyst_recommendation_of_the_month": [],
    }
    for root, _, files in os.walk(directory):
        for filename in files:
            company_name = filename.split("_")[0]
            machine_learning_dataset["company_name"].append(company_name)
            with open(os.path.join(root, filename), "r", encoding="utf-8") as f:
                output_data = json.load(f)

                # info_company
                # si autre société hors us
                # inclure les colonnes  country currency
                info_company = pd.read_json(StringIO(output_data["info_company"]))
                machine_learning_dataset["finnhubIndustry"].append(
                    info_company["finnhubIndustry"].iloc[0]
                )
                machine_learning_dataset["mean_sell"].append(
                    info_company["mean_sell"].iloc[0]
                )
                machine_learning_dataset["mean_strongBuy"].append(
                    info_company["mean_strongBuy"].iloc[0]
                )
                machine_learning_dataset["mean_strongSell"].append(
                    info_company["mean_strongSell"].iloc[0]
                )
                machine_learning_dataset["insider_sentiment"].append(
                    info_company["insider_sentiment"].iloc[0]
                )

                # company_news
                company_posit_dist_percet, company_negat_dist_percet = (
                    get_sentiment_from_news_dataset(
                        news_type="company_news", df=output_data
                    )
                )
                machine_learning_dataset["company_posit_dist_percet"].append(
                    company_posit_dist_percet
                )
                machine_learning_dataset["company_negat_dist_percet"].append(
                    company_negat_dist_percet
                )

                # country_news
                country_posit_dist_percet, country_negat_dist_percet = (
                    get_sentiment_from_news_dataset(
                        news_type="country_news", df=output_data
                    )
                )
                machine_learning_dataset["country_posit_dist_percet"].append(
                    country_posit_dist_percet
                )
                machine_learning_dataset["country_negat_dist_percet"].append(
                    country_negat_dist_percet
                )

                # finance
                breakdown_of_analyst_recommendation = output_data[
                    "historical_stock_info"
                ]["breakdown_of_analyst_recommendation"]
                machine_learning_dataset["analyst_sentiment_distribution"].append(
                    breakdown_of_analyst_recommendation[
                        "distribution_of_recommendations"
                    ]
                )
                machine_learning_dataset["analyst_price_target"].append(
                    breakdown_of_analyst_recommendation["price_targets"]
                )

                # cours bourse
                df = pd.read_json(
                    StringIO(
                        output_data["historical_stock_info"]["today_analyse_price"]
                    )
                )
                machine_learning_dataset["date_bourse"].append(df["Date"].iloc[0])
                # try:
                machine_learning_dataset["open_price"].append(df["Open"].iloc[0])
                machine_learning_dataset["close_price"].append(df["Close"].iloc[0])
                machine_learning_dataset["low_price"].append(df["Low"].iloc[0])
                machine_learning_dataset["high_price"].append(df["High"].iloc[0])
                machine_learning_dataset["volume_action"].append(df["Volume"].iloc[0])
                machine_learning_dataset["this_month_most_direction"].append(
                    df["this_month_most_direction"].iloc[0]
                )
                machine_learning_dataset["last_month_most_direction"].append(
                    df["last_month_most_direction"].iloc[0]
                )
                machine_learning_dataset["year_to_date_direction"].append(
                    df["year_to_date_direction"].iloc[0]
                )
                machine_learning_dataset[
                    "one_year_rolling_period_most_direction"
                ].append(df["one_year_rolling_period_most_direction"].iloc[0])
                machine_learning_dataset[
                    "five_year_rolling_period_most_direction"
                ].append(df["five_year_rolling_period_most_direction"].iloc[0])
                machine_learning_dataset["this_month_trend"].append(
                    df["this_month_trend"].iloc[0]
                )
                machine_learning_dataset["last_month_trend"].append(
                    df["last_month_trend"].iloc[0]
                )
                machine_learning_dataset["year_to_date_trend"].append(
                    df["year_to_date_trend"].iloc[0]
                )
                machine_learning_dataset["one_year_rolling_trend"].append(
                    df["one_year_rolling_trend"].iloc[0]
                )
                machine_learning_dataset["five_year_rollingtrend"].append(
                    df["five_year_rollingtrend"].iloc[0]
                )
                machine_learning_dataset["this_month_volume"].append(
                    df["this_month_volume"].iloc[0]
                )
                machine_learning_dataset["last_month_volume"].append(
                    df["last_month_volume"].iloc[0]
                )
                machine_learning_dataset["year_to_date_volume"].append(
                    df["year_to_date_volume"].iloc[0]
                )
                machine_learning_dataset["one_year_rolling_volume"].append(
                    df["one_year_rolling_volume"].iloc[0]
                )
                machine_learning_dataset["five_year_rolling_volume"].append(
                    df["five_year_rolling_volume"].iloc[0]
                )
                machine_learning_dataset["analyst_recommendation_of_the_month"].append(
                    df["analyst_recommendation_of_the_month"].iloc[0]
                )
        print("Machine learning dataset create")
    return pd.DataFrame(machine_learning_dataset)
