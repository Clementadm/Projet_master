from machine_learning.transform_dataset_ml import transform_dataset
from machine_learning.create_ml_dataset import create_dataset_from_all_file
import numpy as np
import pandas as pd
import pickle
from pathlib import Path


def make_prediction_on_given_company(company_ticker):
    """
    Make an prediction based on the most recent data we got (the day before)
    Use the Model stock in the path model_path = r"Projet_master\mlartifacts\769400862886965147\models\m-34e6065deadd43beaddd155f5f969250\artifacts\model.pkl"
    """
    model_path = r"Projet_master\mlartifacts\769400862886965147\models\m-34e6065deadd43beaddd155f5f969250\artifacts\model.pkl"

    current_path = Path.cwd()
    parent_dir = current_path.parent.absolute()
    full_model_path = parent_dir / model_path
    # print("current_path : ", current_path)
    # print("parent_dir : ", parent_dir)
    # print("full_model_path : ", full_model_path)

    with open(full_model_path, "rb") as file:
        model = pickle.load(file)

    new_data = create_dataset_from_all_file()
    _, X, _, label_encoder = transform_dataset(new_data)
    ticker = company_ticker.lower()
    col = f"company_name_{ticker}"
    filter_company = X[col] == 1
    filter_most_recent_day = X["date_weight"] == 7

    company_most_recent_data = X[filter_company & filter_most_recent_day]
    y_pred = model.predict(company_most_recent_data)
    # print("y_pred", y_pred)
    # print("label_encoder.inverse_transform(y_pred)", label_encoder.inverse_transform(y_pred))
    return label_encoder.inverse_transform(y_pred)[0]
