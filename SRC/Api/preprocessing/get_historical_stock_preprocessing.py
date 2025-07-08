# %%
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
from API.get_data.api_yahoo import (
    get_historical_data,
    get_analyst_price_targets,
    get_business_recommendation,
    get_business_grades,
)
from utils.trends_slope import check_trend_of_price
from utils.trends import get_trends_events
from utils.old_slope import qualify_slope
from collections import Counter


# %%
today = datetime.now()  # .strftime('%Y-%m-%d')
first_of_this_month = today.replace(day=1)
first_of_last_month = first_of_this_month - relativedelta(months=1)

# Remettre l'heure à zéro (minuit)
first_of_this_month_midnight = first_of_this_month.replace(
    hour=0, minute=0, second=0, microsecond=0
)
first_of_last_month_midnight = first_of_last_month.replace(
    hour=0, minute=0, second=0, microsecond=0
)

one_year_rolling = today - relativedelta(months=12)
one_year_rolling_midnight = one_year_rolling.replace(
    hour=0, minute=0, second=0, microsecond=0
)

five_year_rolling = today - relativedelta(year=5)
five_year_rolling_midnight = five_year_rolling.replace(
    hour=0, minute=0, second=0, microsecond=0
)

year_to_date_midnight = datetime(first_of_this_month.year, 1, 1, 0, 0)


# %%
def check_most_present_value_df(df_name):
    value_of_direction = df_name["EMA_Direction_Slope"].values
    most_present_direction = Counter(value_of_direction).most_common(1)[0][0]
    return most_present_direction


# %%
def extract_trend(df_name, col_name: str, degre: int) -> str:
    """
    Computes and qualifies the slope trend of a given column in the DataFrame.

    Args:
        df_name (pd.DataFrame): Filtered DataFrame to analyze.
        col (str): Column name to compute the trend on.
        degre (int): Degree for the polynomial fit. Default is 3.

    Returns:
        str: The trend label : Very bullish, Bullish, Stagnant, Bearish, Very bearish
    """
    slope = get_trends_events(df=df_name, cols=[col_name], degre=degre)
    slope_value = slope[f"{col_name}_slope"]
    return qualify_slope(slope_value)["steepness"]


# %%
def breakdown_of_analyst_recommendation(business_ticker):
    business_grades_tab = get_business_grades(business_ticker)
    last_recommendation_by_firm = business_grades_tab.drop_duplicates(
        subset="Firm", keep="first"
    )
    lst_recomd_one_y_rolling = last_recommendation_by_firm[
        last_recommendation_by_firm["GradeDate"] > one_year_rolling_midnight
    ]

    # Remplacement des mentions textuelles spécifiques par une note équivalente (ici 1)
    replace_map = {"Sector Weight": 1, "Sector Outperform": 1}

    # Application des remplacements uniquement sur les valeurs correspondantes
    lst_recomd_one_y_rolling.loc[:, "ToGrade"] = lst_recomd_one_y_rolling[
        "ToGrade"
    ].replace(replace_map)
    lst_recomd_one_y_rolling.loc[:, "ToGrade"] = (
        pd.to_numeric(lst_recomd_one_y_rolling["ToGrade"], errors="coerce")
        .fillna(pd.NA)
        .astype(int)
    )

    # Moyenne pondérée des ToGrade pour refléter le consensus global
    sentiment_moyen = lst_recomd_one_y_rolling["ToGrade"].mean()
    print(f"Sentiment moyen des analystes : {sentiment_moyen:.2f}")

    # Pourcentage d’avis positifs, neutres et négatifs
    positifs = (lst_recomd_one_y_rolling["ToGrade"] == 1).mean() * 100
    negatifs = (lst_recomd_one_y_rolling["ToGrade"] == 0).mean() * 100

    return {
        "distribution_of_recommendations": {
            "positif": format(positifs, ".2f"),
            "negatifs": format(negatifs, ".2f"),
        },
        "price_targets": get_analyst_price_targets(business_ticker),
    }


# %%
def historical_stock_info(business_ticker):
    df = get_historical_data(business_ticker, "5y")

    # Reset date to LocalTime
    df["Date"] = df["Date"].apply(lambda x: x.tz_localize(None))

    # filter Dataframe
    this_month_data = df[df["Date"] >= first_of_this_month_midnight]
    last_month_data = df[df["Date"] >= first_of_last_month_midnight]
    year_to_date_data = df[df["Date"] >= year_to_date_midnight]
    one_year_rolling_period_data = df[df["Date"] >= one_year_rolling_midnight]
    five_year_rolling_period_data = df[df["Date"] >= five_year_rolling_midnight]
    different_dataframe_filter_bydate = [
        this_month_data,
        last_month_data,
        year_to_date_data,
        one_year_rolling_period_data,
        five_year_rolling_period_data,
    ]

    # analyse today price
    return_df = df[["Date", "Close", "Volume"]].tail(1)
    all_trends = []
    all_volume = []
    # compute trend price and volume
    for df_filter in different_dataframe_filter_bydate:
        check_trend_of_price(df_filter)
        trend_price = extract_trend(df_name=df_filter, col_name="Close", degre=3)
        all_trends.append(trend_price)
        trend_volume = extract_trend(df_name=df_filter, col_name="Volume", degre=3)
        all_volume.append(trend_volume)

    # allocate the most sxitch there have been during an period (up, down, flat)
    return_df["this_month_most_direction"] = check_most_present_value_df(
        this_month_data
    )
    return_df["last_month_most_direction"] = check_most_present_value_df(
        last_month_data
    )
    return_df["year_to_date_direction"] = check_most_present_value_df(year_to_date_data)
    return_df["one_year_rolling_period_most_direction"] = check_most_present_value_df(
        one_year_rolling_period_data
    )
    return_df["five_year_rolling_period_most_direction"] = check_most_present_value_df(
        five_year_rolling_period_data
    )

    # Allocate all trends calculate
    return_df["this_month_trend"] = all_trends[0]
    return_df["last_month_trend"] = all_trends[1]
    return_df["year_to_date_trend"] = all_trends[2]
    return_df["one_year_rolling_trend"] = all_trends[3]
    return_df["five_year_rollingtrend"] = all_trends[4]

    return_df["this_month_volume"] = all_volume[0]
    return_df["last_month_volume"] = all_volume[1]
    return_df["year_to_date_volume"] = all_volume[2]
    return_df["one_year_rolling_volume"] = all_volume[3]
    return_df["five_year_rolling_volume"] = all_volume[4]

    # Analyst recommendation
    df_business_recommendation = get_business_recommendation("MSFT")
    rating_of_month = df_business_recommendation[
        ["strongBuy", "buy", "hold", "sell", "strongSell"]
    ].loc[0]
    best_rating = rating_of_month.idxmax()
    return_df["analyst_recommendation_of_the_month"] = (
        best_rating  # ["strongBuy", "buy", "hold", "sell", "strongSell"]
    )

    analyst_info = breakdown_of_analyst_recommendation(business_ticker)

    return {
        "today_analyse_price": return_df.to_json(),
        # "today_analyse_price": return_df.to_json(),
        "breakdown_of_analyst_recommendation": analyst_info,
    }


# %%
# a = historical_stock_info("MSFT")
