# %%
import yfinance as yf
from typing import Literal
import pandas as pd


# %%
def get_business_recommendation(business_name):
    business = yf.Ticker(business_name)
    df = pd.json_normalize(business.info)
    df = df[
        [
            "address1",
            "city",
            "state",
            "zip",
            "country",
            "phone",
            "website",
            "sector",
            "previousClose",
            "open",
            "dayLow",
            "dayHigh",
            "regularMarketPreviousClose",
            "regularMarketOpen",
            "regularMarketDayLow",
            "regularMarketDayHigh",
            "volume",
            "regularMarketVolume",
            "bid",
            "ask",
            "bidSize",
            "askSize",
            "returnOnEquity",
            "earningsGrowth",
            "revenueGrowth",
            "grossMargins",
            "ebitdaMargins",
            "operatingMargins",
            "ebitda",
            "totalDebt",
            "quickRatio",
            "lastDividendValue",
            "lastDividendDate",
            "currentPrice",
            "targetHighPrice",
            "targetLowPrice",
            "targetMeanPrice",
            "targetMedianPrice",
            "recommendationMean",
            "recommendationKey",
            "numberOfAnalystOpinions",
        ]
    ]
    return df


# get_business_recommendation("AAPL")


# %%
def get_calendar(business_name):
    business = yf.Ticker(business_name)
    df = pd.json_normalize(business.calendar)
    return df


# get_calendar("AAPL")


# %%
def get_historical_data(business_name: str, period_choose: str) -> None:
    business = yf.Ticker(business_name)
    trade_hist = business.history(period=period_choose)
    trade_hist = trade_hist.reset_index()
    trade_hist["Date"] = pd.to_datetime(trade_hist["Date"])
    trade_hist["Year"] = trade_hist["Date"].apply(lambda x: x.year)
    trade_hist["Month"] = trade_hist["Date"].apply(lambda x: x.month)
    trade_hist["Day"] = trade_hist["Date"].apply(lambda x: x.day)
    trade_hist = trade_hist[
        [
            "Date",
            "Year",
            "Month",
            "Day",
            "Open",
            "High",
            "Low",
            "Close",
            "Volume",
            "Dividends",
            "Stock Splits",
        ]
    ]
    return trade_hist


# get_historical_data("AAPL", "3mo")


# %%
def get_analyst_price_targets(business_name):
    business = yf.Ticker(business_name)
    analyst_price_targets = business.analyst_price_targets
    return analyst_price_targets


# get_analyst_price_targets("AAPL")


# %%
def get_business_recommendation(business_name):
    business = yf.Ticker(business_name)
    recommendation = business.recommendations
    return recommendation


# get_business_recommendation("AAPL")


# %%
def get_business_grades(business_name):
    business = yf.Ticker(business_name)
    grade = business.upgrades_downgrades
    grade = grade.reset_index()

    grade["GradeDate"] = pd.to_datetime(grade["GradeDate"])
    grade["GradeYear"] = grade["GradeDate"].apply(lambda x: x.year)
    grade["GradeMonth"] = grade["GradeDate"].apply(lambda x: x.month)
    grade["GradeDay"] = grade["GradeDate"].apply(lambda x: x.day)

    grade[
        [
            "GradeDate",
            "GradeMonth",
            "GradeDay",
            "GradeYear",
            "Firm",
            "ToGrade",
            "FromGrade",
            "Action",
        ]
    ]

    # 1. Catégorie Positive : Ces termes indiquent une perspective optimiste pour l’action, suggérant d’acheter ou de surpondérer :
    # 2. Catégorie Neutre : Ces termes indiquent une perspective équilibrée, conseillant souvent de garder ou de ne pas agir de manière significative :
    # 3. Catégorie Négative : Ces termes reflètent une opinion pessimiste, recommandant de vendre ou de réduire l’exposition :

    # Les recommandations positives encouragent les investisseurs à acheter ou à renforcer leur position.
    ##  Les recommandations neutres suggèrent d’attendre sans prendre de décision précipitée.
    # Les recommandations négatives avertissent que l’action pourrait sous-performer et indiquent souvent de vendre ou de réduire sa position.

    grade["ToGrade"] = grade["ToGrade"].replace(
        [
            "Buy",
            "Strong Buy",
            "Outperform",
            "Overweight",
            "Neutral",
            "Hold",
            "Market Perform",
            "Equal-Weight",
            "Sector Perform",
            "Perform",
            "Sell",
            "Underperform",
            "Underweight",
        ],
        [
            "Positif",
            "Positif",
            "Positif",
            "Positif",
            "Neutre",
            "Neutre",
            "Neutre",
            "Neutre",
            "Neutre",
            "Neutre",
            "Negative",
            "Negative",
            "Negative",
        ],
    )

    grade["ToGrade"] = grade["ToGrade"].replace(
        ["Positif", "Neutre", "Negative"], [1, 0, -1]
    )

    grade = grade.reset_index()

    return grade


# get_business_grades("AAPL")


# %% [markdown]
# avoir la range du strike prix min, max et median
# le nombre d'option
#
# permet apres de svaoir si le prix de laction est :
# - au dessus des prix des options → mauvais signe pas achete
# - en desous → bonne affaire
# - moyenne → bonne affaire
# - median → neutre, pas acheter
#
# si beaucoup d'option de ventes pas acheter
# si beaucoup option d'achat, acheter


# %%
def get_options(business_name):
    """
    Récuperation de toutes les options avec toutes les dates d'expiration connus
    call → Une option CALL donne à l'acheteur le droit (mais pas l'obligation) d'ACHETER l'actif sous-jacent à un prix prédéfini avant ou à la date d'expiration
    put → Une option PUT donne à l'acheteur le droit (mais pas l'obligation) de VENDRE l'actif sous-jacent à un prix prédéfini avant ou à la date d'expiration
    """
    business = yf.Ticker(business_name)

    # Récupérer les dates d'expiration disponibles
    expiration_dates = business.options

    # liste pour stocker les données d'options
    options_data = []

    for date in expiration_dates:
        # Récupérer les chaines d'options pour cette date
        opt_chain = business.option_chain(date)

        # Ajouter les calls et puts + col pour date et type
        calls = opt_chain.calls
        calls["expirationDate"] = date
        calls["Type"] = "calls"

        puts = opt_chain.puts
        puts["expirationDate"] = date
        puts["Type"] = "puts"

        options_data.append(calls)
        options_data.append(puts)

    # Combiner toutes les données en un seul DataFrame
    options_df = pd.concat(options_data, ignore_index=True)
    return options_df


# get_options("AAPL")
