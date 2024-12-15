# %%
import os
import json

# %%
parent_dir = os.path.abspath(os.path.join("../../", "API_KEYS.json"))
with open(parent_dir, "r") as fichier:
    # Charger le contenu du fichier JSON dans une variable
    data = json.load(fichier)

# %%
API_KEY_NEWS = data["API"][1]["NewsAPI"]
API_KEY_FINNHUB = data["API"][0]["FinnHub"]
