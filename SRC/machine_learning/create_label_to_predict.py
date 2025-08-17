import math

# On donne un poids à chaque colonne de notre dataframe
# ce poids est pondéré selon l'importance de la colonne et ce dont on veut lui donner comme importance.
# Ce poids est stocké dans une variable
# est a la fin selon la valeur de ce poids on attribué une valeur textuel (hold, buy, sell)


# %%
def create_label_from_scoring(row):
    """
    Calculates an investment score and returns the decision (buy/sell/hold)
    + details of the points awarded by criterion.
    """
    score = 0.0
    details = []

    def add(critere, points, raison):
        nonlocal score, details
        score += points
        details.append(
            {"critere": critere, "score": round(points, 3), "raison": raison}
        )

    # Analyst sentiment distribution
    analyst_sentiment_distribution = row.get("analyst_sentiment_distribution")
    mean_sentiment = analyst_sentiment_distribution.get("mean_sentiment")

    def scoring_analys_distribution(mean_sentiment_value):
        score_analys_dist = 0
        if isinstance(mean_sentiment_value, (int, float)) and not math.isnan(
            mean_sentiment_value
        ):
            if mean_sentiment_value > 0.25:
                score_analys_dist = 0.5
            elif mean_sentiment_value > 0.75:
                score_analys_dist = 1
            elif mean_sentiment_value < 0.25:
                score_analys_dist = -0.5
            elif mean_sentiment_value < 0.75:
                score_analys_dist = -1
            else:
                score_analys_dist = 0
        return score_analys_dist

    add(
        "Analyst sentiment distribution",
        scoring_analys_distribution(float(mean_sentiment)),
        f"mean_sentiment = {mean_sentiment}",
    )

    # Analyst recommendation
    ############################################
    analyst_recommendation = str(
        row.get("analyst_recommendation_of_the_month", "")
    ).lower()
    if analyst_recommendation == "strongBuy":
        add("Analyst recommendation", +3, "Reco du mois = strongBuy")
    elif analyst_recommendation == "buy":
        add("Analyst recommendation", +1, "Reco du mois = buy")
    elif analyst_recommendation == "strongSell":
        add("Analyst recommendation", -3, "Reco du mois = strongSell")
    elif analyst_recommendation == "sell":
        add("Analyst recommendation", -1, "Reco du mois = sell")
    else:  # case analyst_recommendation == hold
        add(
            "Analyst recommendation",
            0,
            f"Reco du mois = {analyst_recommendation or 'N/A'}",
        )

    # Strong Sell and Strong Buy distribution
    ############################################
    mean_strong_buy = row.get("mean_strongBuy")
    if isinstance(mean_strong_buy, (int, float)) and not math.isnan(mean_strong_buy):
        add(
            "StrongBuy distribution",
            mean_strong_buy,
            f"mean_strongBuy={mean_strong_buy}",
        )
    mean_strong_sell = row.get("mean_strongSell")

    if isinstance(mean_strong_sell, (int, float)) and not math.isnan(mean_strong_sell):
        add(
            "StrongSell distribution",
            -mean_strong_sell,
            f"mean_strongSell={-mean_strong_sell}",
        )

    # Analyste Price Target
    ############################################
    analyst_price_target = row.get("analyst_price_target") or {}
    current_price = analyst_price_target.get("current")
    low_price = analyst_price_target.get("low")
    high_price = analyst_price_target.get("high")
    median_price = analyst_price_target.get("median")
    mean_price = analyst_price_target.get("mean")
    if (
        isinstance(low_price, (int, float))
        and not math.isnan(low_price)
        and current_price != 0
    ):
        gap_low_current = (low_price - current_price) / current_price
        add(
            "Gap between actual price and the LOW analyst price target",
            gap_low_current,
            f"({low_price} - {current_price}) / {current_price}={gap_low_current}",
        )

    if (
        isinstance(high_price, (int, float))
        and not math.isnan(high_price)
        and current_price != 0
    ):
        gap_high_current = (high_price - current_price) / current_price
        add(
            "Gap between actual price and the HIGH analyst price target",
            gap_high_current,
            f"({high_price} - {current_price}) / {current_price}={gap_high_current}",
        )

    if (
        isinstance(median_price, (int, float))
        and not math.isnan(median_price)
        and current_price != 0
    ):
        gap_median_current = (median_price - current_price) / current_price
        add(
            "Gap between actual price and the MEDIAN analyst price target",
            gap_median_current,
            f"({median_price} - {current_price}) / {current_price}={gap_median_current}",
        )

    if (
        isinstance(mean_price, (int, float))
        and not math.isnan(mean_price)
        and current_price != 0
    ):
        gap_mean_current = (mean_price - current_price) / current_price
        add(
            "Gap between actual price and the MEAN analyst price target",
            gap_mean_current,
            f"({mean_price} - {current_price}) / {current_price}={gap_mean_current}",
        )

    # Price and volume tendance
    ############################################
    def compute_tendance_score(trend_value: str) -> float:
        if not isinstance(trend_value, str):
            return 0.0
        if "Very bullish" in trend_value:
            return +2
        if "Bullish" in trend_value:
            return +0.5
        if "Stagnant" in trend_value:
            return 0
        if "Bearish" in trend_value:
            return -0.5
        if "Very bearish" in trend_value:
            return -2

    # price
    for col_price_trend, label_price_trend in [
        ("this_month_trend", "Price Trend (this month)"),
        ("last_month_trend", "Price Trend (last month)"),
        ("year_to_date_trend", "Price Trend (YTD)"),
        ("one_year_rolling_trend", "Price Trend (1Y rolling)"),
        ("five_year_rollingtrend", "Price Trend (5Y rolling)"),
    ]:
        price_trend = row.get(col_price_trend)
        price_tendance_score = compute_tendance_score(price_trend)
        add(label_price_trend, price_tendance_score, f"{col_price_trend}={price_trend}")

    # Volume
    for col_volume_trend, label_volume_trend in [
        ("this_month_volume", "Volume Trend (this month)"),
        ("last_month_volume", "Volume Trend (last month)"),
        ("year_to_date_volume", "Volume Trend (YTD)"),
        ("one_year_rolling_volume", "Volume Trend (1Y rolling)"),
        ("five_year_rolling_volume", "Volume Trend (5Y rolling)"),
    ]:
        volume_trend = row.get(col_volume_trend)
        price_tendance_score = compute_tendance_score(volume_trend)
        add(
            label_volume_trend,
            price_tendance_score,
            f"{col_volume_trend}={volume_trend}",
        )

    # Direction slope
    ############################################
    def compute_slope_direction_score(slope_value: str) -> float:
        if not isinstance(slope_value, str):
            return 0.0
        if "Up" in slope_value:
            return +1
        if "Down" in slope_value:
            return -1
        if "Flat" in slope_value:
            return 0

    for col_direction, label_direction in [
        ("this_month_most_direction", "Most slope direction (this month)"),
        ("last_month_most_direction", "Most slope direction (last month)"),
        ("year_to_date_direction", "Most slope direction (YTD)"),
        ("one_year_rolling_period_most_direction", "Most slope direction (1Y rolling)"),
        (
            "five_year_rolling_period_most_direction",
            "Most slope direction (5Y rolling)",
        ),
    ]:
        direction = row.get(col_direction)
        slope_direction_score = compute_slope_direction_score(direction)
        add(label_direction, slope_direction_score, f"{col_direction}={direction}")

    # Sentiment news score
    ############################################
    def sentiment_analys_diferrence(positif_col, negative_col, news_type):
        positif_sent = row.get(positif_col)
        negatif_sent = row.get(negative_col)
        if isinstance(positif_sent, (int, float)) and isinstance(
            negatif_sent, (int, float)
        ):
            diff = positif_sent - negatif_sent
            if diff >= 0.25:
                add(f"{news_type} news sentiment", +0.5, f"diff={diff:.2f} ≥ 0.25")
            elif diff <= -0.25:
                add(f"{news_type} news sentiment", -0.5, f"diff={diff:.2f} ≤ -0.25")
            else:
                add(f"{news_type} news sentiment", 0, f"diff={diff:.2f} neutre")

    sentiment_analys_diferrence(
        positif_col="company_posit_dist_percet",
        negative_col="company_negat_dist_percet",
        news_type="Company",
    )
    sentiment_analys_diferrence(
        positif_col="country_posit_dist_percet",
        negative_col="country_negat_dist_percet",
        news_type="Country",
    )

    # E. Insider sentiment
    ############################################
    insider_sentiment = row.get("insider_sentiment")
    if isinstance(insider_sentiment, (int, float)):
        add(
            "Insider sentiment",
            insider_sentiment,
            f"insider_sentiment={insider_sentiment}",
        )
    else:
        add(
            "Insider sentiment",
            0,
            f"Value of insider sentiment unavailable ={insider_sentiment}",
        )

    # Final Scoring
    ############################################
    decision = "hold"
    if score >= 1.5:
        decision = "buy"
    elif score <= -1.5:
        decision = "sell"

    return {
        "decision": decision,
        "score_total": round(score, 3),
        "details": details
    }
