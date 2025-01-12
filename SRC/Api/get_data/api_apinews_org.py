# %%
import os
import sys
from pathlib import Path

# current_dir = os.getcwd()
# sys.path.append(str(Path(current_dir).parent))

# from get_api_keys import API_KEY_NEWS
from .get_api_keys import API_KEY_NEWS
import requests
from datetime import datetime, timedelta
import pandas as pd

# %% [markdown]
# # <h1 style="color:red"> APINEWS.ORG

# %% [markdown]
# **sources=bloomberg,cnbc**
# **language=fr** pour obtenir uniquement des articles en français.


# %%
def get_news(business_name, anteriorite_en_jours):
    from_date = (datetime.now() - timedelta(days=anteriorite_en_jours)).strftime(
        "%Y-%m-%d"
    )  # Exemple : articles des 7 derniers jours
    print(f"Date des articles de récupération des articles {from_date}")
    # sortBy=popularity : articles from popular sources and publishers come first
    # sortBy=relevancy : articles more closely related to q come first
    # sortBy=publishedAt : newest articles come first.

    # searchIn The fields to restrict your q search to. can be separet by an comma
    # title
    # description
    # content

    # on cherche le nom de la companie dans le titre de l'article
    # aves des articles du nombre de jours d'aujorunhuit - anteriorite_en_jours
    # trier par articles plus populaire en premier
    # uniquements
    url = f"https://newsapi.org/v2/everything?q={business_name}&searchIn=title&from={from_date}&sortBy=popularity&apiKey={API_KEY_NEWS}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "ok":
        return pd.json_normalize(data["articles"])
    else:
        return print("Erreur:", data.get("message"))


# # %%
# all_news = get_news(business_name="tesla", anteriorite_en_jours=7)

# # %%
# all_news.head(2)
