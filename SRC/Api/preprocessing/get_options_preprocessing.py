# %% [markdown]
#     call → Une option CALL donne à l'acheteur le droit (mais pas l'obligation) d'ACHETER l'actif sous-jacent à un prix prédéfini avant ou à la date d'expiration
#     put → Une option PUT donne à l'acheteur le droit (mais pas l'obligation) de VENDRE l'actif sous-jacent à un prix prédéfini avant ou à la date d'expiration

# %%
from API.get_data.api_yahoo import get_options
import pandas as pd
from API.get_data.api_yahoo import get_analyst_price_targets

# %%
# CLASSIFICATION_RANGES = [
#     (-float("inf"), -25, "Very undervalued"), # Très sous-évalué
#     (-25, -5, "Slightly undervalued"), # Légèrement sous-évalué
#     (-5, 5, "Price within spread"), # Prix dans le spread
#     (5, 25, "Slightly overvalued"), # Légèrement surévalué
#     (25, float("inf"), "Very overvalued"), #Très surévalué
# ]

# Réevaluation des seuils (seuil en pourcentage)
##############################################
CLASSIFICATION_RANGES = [
    (-float("inf"), -4, "Very undervalued"), # Très sous-évalué
    (-4, -2, "Slightly undervalued"), # Légèrement sous-évalué
    (-2, 2, "Price within spread"), # Prix dans le spread
    (2, 4, "Slightly overvalued"), # Légèrement surévalué
    (4, float("inf"), "Very overvalued"), #Très surévalué
]


def classify_spread(spread_ratio):
    """
    Classify the spread ratio into predefined clusters.

    Args:
        spread_ratio (float): The spread ratio to classify.

    Returns:
        str: The cluster classification.
    """
    return next(
        (cluster for lower, upper, cluster in CLASSIFICATION_RANGES if lower <= spread_ratio < upper),
        "Non classifié",  # Default case
    )


# %%
# approche liquidité et la pression acheteur/vendeur des options via le spread bid-ask pondéré par le volume

# Si spread ratio fortement positif → Le prix moyen pondéré des asks est bien plus élevé que celui des bids → Très surévalué (Very overpriced).
# Si spread ratio légèrement positif → Déséquilibre modéré → Légèrement surévalué (Slightly overpriced).
# Si spread ratio proche de 0 → offre et demande équilibrées → Prix dans le spread (Price within spread).
# Si spread ratio légèrement négatif → Déséquilibre en faveur des acheteurs → Légèrement sous-évalué (Slightly undervalued).
# Si spread ratio fortement négatif → La pression acheteuse très forte → Très sous-évalué (Very undervalued).

def get_options_cluster(df):
    """
    Determine the market expectations of the company via these options. Those options can be :
        - Very undervalued
        - Slightly undervalued
        - Price within spread
        - Slightly overpriced
        - Very overpriced
    If is undervalued → sould buy
    If is overvalued → sould not buy

    Args:
        df (dataframe): the dataframe to classify

    Returns:
        str: the cluster.
    """

    # Weighted average by option volume
    # weighted average = sum(price * volume) / sum of volumes
    # goal is to reflect the relative importance of each option by taking volumes into account
    mean_weighted_ask = (df["ask"] * df["volume"]).sum() / df["volume"].sum()
    mean_weighted_bid = (df["bid"] * df["volume"]).sum() / df["volume"].sum()
    # print(mean_weighted_ask)
    # print(mean_weighted_bid)

    spread_ratio = ((mean_weighted_ask - mean_weighted_bid) / (mean_weighted_ask + mean_weighted_bid)) * 100

    # for lower_value, upper_value, cluster in CLASSIFICATION_RANGES:
    #     if lower_value <= spread_ratio < upper_value:
    #         return cluster
    # return "Non classifié"  # Cas par défaut (ne devrait pas arriver)
    return classify_spread(spread_ratio)
    

# %%
def create_options_dataset(business_ticker):
    options = get_options(business_ticker)

    # Divide in puts and calls option type
    puts = options[(options["Type"]=="puts") & (options["ask"]>0)]
    calls = options[(options["Type"]=="calls") & (options["ask"]>0)]

    # Filter NaN values on ask, bid and volume cols
    filter_volume_nan = (options["volume"].isna() == False) 
    filter_bid_nan = (options["bid"].isna() == False) 
    filter_ask_nan = (options["ask"].isna() == False)

    options = options[filter_volume_nan & filter_bid_nan & filter_ask_nan]

    # Compute cluster by option type
    cluster_buy = get_options_cluster(calls)
    cluster_sell = get_options_cluster(puts)

    # Compute number of line per options type
    nb_option_buy = calls.shape[0]
    nb_option_sell = puts.shape[0]

    # Get analyste price target and actual price 
    analyst_price_targets = get_analyst_price_targets("TSLA")

    # mean volume
    buy_mean_volume = calls["volume"].mean()
    sell_mean_volume = puts["volume"].mean()

    return pd.DataFrame({
        "cluster_buy":[cluster_buy],
        "cluster_sell":[cluster_sell],
        "nb_option_buy":[nb_option_buy],
        "nb_option_sell":[nb_option_sell],
        "buy_mean_volume":[buy_mean_volume],
        "sell_mean_volume":[sell_mean_volume],
        'current_price': analyst_price_targets["current"],
        'low_analyst_price_targets': analyst_price_targets["low"],
        'high_analyst_price_targets': analyst_price_targets["high"],
        'mean_analyst_price_targets': analyst_price_targets["mean"],
        'median_analyst_price_targets': analyst_price_targets["median"]
    })   


# %%
# a = create_options_dataset("TSLA")
# a


