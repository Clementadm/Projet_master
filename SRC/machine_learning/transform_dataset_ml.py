# %%
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from machine_learning.create_label_to_predict import create_label_from_scoring


# %%
def replace_direction_value(value):
    """Replace direction value from str to int"""
    if value == "Down":
        return -1
    elif value == "Up":
        return 1
    elif value == "Flat":
        return 0


# %%
def replace_trend_value(trend_value):
    """Replace trend value from str to int"""
    if "Very bullish" in trend_value:
        return 2
    if "Bullish" in trend_value:
        return 1
    if "Stagnant" in trend_value:
        return 0
    if "Bearish" in trend_value:
        return -1
    if "Very bearish" in trend_value:
        return -2


# %%
def date_weight(dataset, starting_weight):
    """
    Each line is assigned a decreasing weight based on the date value (most recent = +2, then +1, then 0, then -1, etc.).
    Inputs:
        - starting_weight : weitht assigned for the most recent date
        - dataset: dataset where date_bourse is prensent and have to be changed
    """
    dataset_copy = dataset.copy()
    ranks = (
        dataset_copy["date_bourse"].rank(ascending=False, method="dense").astype(int)
    )
    dataset_copy["date_weight"] = (starting_weight + 1) - ranks
    return dataset_copy["date_weight"]


# %%
def transform_dataset(dataset):
    # df["decision_pack"] contiendra {decision, score_total, details}
    dataset["decision_pack"] = dataset.apply(
        lambda x: create_label_from_scoring(x.to_dict()), axis=1
    )

    # Colonnes pratiques à parser
    dataset["decision_label"] = dataset["decision_pack"].apply(lambda d: d["decision"])
    dataset["decision_score"] = dataset["decision_pack"].apply(
        lambda d: d["score_total"]
    )

    # replace direction value by 0, -1 or 1
    dataset["this_month_most_direction"] = dataset["this_month_most_direction"].apply(
        lambda x: replace_direction_value(x)
    )
    dataset["last_month_most_direction"] = dataset["last_month_most_direction"].apply(
        lambda x: replace_direction_value(x)
    )
    dataset["year_to_date_direction"] = dataset["year_to_date_direction"].apply(
        lambda x: replace_direction_value(x)
    )
    dataset["one_year_rolling_period_most_direction"] = dataset[
        "one_year_rolling_period_most_direction"
    ].apply(lambda x: replace_direction_value(x))
    dataset["five_year_rolling_period_most_direction"] = dataset[
        "five_year_rolling_period_most_direction"
    ].apply(lambda x: replace_direction_value(x))

    # replace price trend value
    dataset["this_month_trend"] = dataset["this_month_trend"].apply(
        lambda x: replace_trend_value(x)
    )
    dataset["last_month_trend"] = dataset["last_month_trend"].apply(
        lambda x: replace_trend_value(x)
    )
    dataset["year_to_date_trend"] = dataset["year_to_date_trend"].apply(
        lambda x: replace_trend_value(x)
    )
    dataset["one_year_rolling_trend"] = dataset["one_year_rolling_trend"].apply(
        lambda x: replace_trend_value(x)
    )
    dataset["five_year_rollingtrend"] = dataset["five_year_rollingtrend"].apply(
        lambda x: replace_trend_value(x)
    )

    # replace volume trend value
    dataset["this_month_volume"] = dataset["this_month_volume"].apply(
        lambda x: replace_trend_value(x)
    )
    dataset["last_month_volume"] = dataset["last_month_volume"].apply(
        lambda x: replace_trend_value(x)
    )
    dataset["year_to_date_volume"] = dataset["year_to_date_volume"].apply(
        lambda x: replace_trend_value(x)
    )
    dataset["one_year_rolling_volume"] = dataset["one_year_rolling_volume"].apply(
        lambda x: replace_trend_value(x)
    )
    dataset["five_year_rolling_volume"] = dataset["five_year_rolling_volume"].apply(
        lambda x: replace_trend_value(x)
    )

    # analyst_mean_sentiment_distribution to float between 0 and 1
    dataset["analyst_mean_sentiment_distribution"] = dataset[
        "analyst_sentiment_distribution"
    ].apply(lambda x: float(x["mean_sentiment"]))
    dataset["analyst_positif_sentiment_distribution"] = dataset[
        "analyst_sentiment_distribution"
    ].apply(lambda x: float(x["positif"]) / 100)
    dataset["analyst_negatif_sentiment_distribution"] = dataset[
        "analyst_sentiment_distribution"
    ].apply(lambda x: float(x["negatifs"]) / 100)
    dataset.drop(columns=["analyst_sentiment_distribution"], axis=1, inplace=True)

    # Price target analyst
    dataset["current_price"] = dataset["analyst_price_target"].apply(
        lambda x: x["current"]
    )
    dataset["high_price_target"] = dataset["analyst_price_target"].apply(
        lambda x: x["high"]
    )
    dataset["low_price_target"] = dataset["analyst_price_target"].apply(
        lambda x: x["low"]
    )
    dataset["mean_price_target"] = dataset["analyst_price_target"].apply(
        lambda x: x["mean"]
    )
    dataset["median_price_target"] = dataset["analyst_price_target"].apply(
        lambda x: x["median"]
    )
    dataset.drop(columns=["analyst_price_target"], axis=1, inplace=True)

    # Date from datetime to int decreasing
    dataset["date_weight"] = date_weight(dataset, starting_weight=7)

    # Encoding X and y
    # X
    one_hot_enc = OneHotEncoder(sparse_output=False).set_output(transform="pandas")
    col_enc = one_hot_enc.fit_transform(
        dataset[
            ["company_name", "finnhubIndustry", "analyst_recommendation_of_the_month"]
        ]
    )
    dataset.drop(
        columns=[
            "company_name",
            "finnhubIndustry",
            "analyst_recommendation_of_the_month",
        ],
        axis=1,
        inplace=True,
    )

    # y
    label_encoder = LabelEncoder()
    label = dataset["decision_label"]
    values = label_encoder.fit_transform(label)
    dataset["decision_label"] = values

    X = pd.concat([col_enc, dataset], axis=1).drop(
        ["date_bourse", "decision_label", "decision_pack"], axis=1
    )
    y = values
    return dataset, X, y, label_encoder
