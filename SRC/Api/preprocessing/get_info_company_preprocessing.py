# %%
import pandas as pd
import numpy as np 
from API.get_data.api_finnhub import get_competitor, recommendation_trends, insider_sentiment, info_company
from datetime import datetime, timedelta

# %%
def summarize_recommendation_trends(business_ticker):
    df_trend = recommendation_trends(business_ticker)
    # Compute recommendation trend
    # Put all the value between 0 and 1 by taking acount the nmber of analyst recommendation for one date 
    total_recommendation = df_trend["sell"] + df_trend["strongBuy"] + df_trend["strongSell"]
    df_trend["sell"] = df_trend["sell"] / total_recommendation
    df_trend["strongBuy"] = df_trend["strongBuy"] / total_recommendation
    df_trend["strongSell"] = df_trend["strongSell"] / total_recommendation
    mean_sell = np.round(df_trend["sell"].mean(),2)
    mean_strongBuy = np.round(df_trend["strongBuy"].mean(),2)
    mean_strongSell = np.round(df_trend["strongSell"].mean(),2)

    # Compute date
    period_max = df_trend["period"].max()
    period_min = df_trend["period"].min()

    df_return = pd.DataFrame({
        "begin_analyst_period": [period_min],
        "end_analyst_period": [period_max],
        "delta_number_days_analyst": [(pd.to_datetime(period_max) - pd.to_datetime(period_min)).days],
        "mean_sell" : [mean_sell],
        "mean_strongBuy" : [mean_strongBuy],
        "mean_strongSell" : [mean_strongSell]
    })
    return df_return

# %%
def calcul_tendance_insider(business_ticker):
    """
    Evaluates the evolution of the mspr over a 365-day period to determine whether it is improving or deteriorating  
    If improving ==> 1 
    If deteriorating ==> -1
    """

    from_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    today = datetime.now().strftime('%Y-%m-%d')
    df_insider_sentiment = insider_sentiment(business_ticker, from_date, today)

    x = df_insider_sentiment["mspr"].index
    y = df_insider_sentiment["mspr"].values

    # Calcul de la régression linéaire avec numpy (en utilisant la méthode des moindres carrés)
    # y = a * x + b, où a est la pente et b l'ordonnée à l'origine
    a, b = np.polyfit(x, y, 1)

    # Calculer les valeurs lissées de y
    y_lisse = a * x + b

    calcul_degre_pente = y_lisse[-1] - y_lisse[0]
    if calcul_degre_pente >0:
        return 1 # courbe croissante 
    else:
        return -1 # courbe décroissante 

# %%
# get_competitor("TSLA")

# # %%
# summarize_recommendation_trends("TSLA")

# # %%
# calcul_tendance_insider("TSLA")

# # %%
# info_company("TSLA")

# %%
def get_info_company_preprocessing(business_ticker):
    competitor_lst = get_competitor(business_ticker)
    info_company_df = info_company(business_ticker)
    trend_recommendation_summarized = summarize_recommendation_trends(business_ticker)
    df_return = info_company_df
    df_return["competitor_lst"] = ', '.join(competitor_lst)
    df_return["begin_analyst_period"] = trend_recommendation_summarized["begin_analyst_period"]
    df_return["end_analyst_period"] = trend_recommendation_summarized["end_analyst_period"]
    df_return["delta_number_days_analyst"] = trend_recommendation_summarized["delta_number_days_analyst"]
    df_return["mean_sell"] = trend_recommendation_summarized["mean_sell"]
    df_return["mean_strongBuy"] = trend_recommendation_summarized["mean_strongBuy"]
    df_return["mean_strongSell"] = trend_recommendation_summarized["mean_strongSell"]
    df_return["insider_sentiment"] = calcul_tendance_insider(business_ticker) #1 = sentiment improving / -1 = sentiment deteriorating 
    # return df_return 
    return df_return.to_json()

# %%
# u = get_info_company_preprocessing("TSLA")
# u
