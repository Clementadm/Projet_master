import pandas as pd
import json


def read_json_file(data):
    parsed = json.loads(data)
    df = pd.DataFrame.from_dict(parsed)
    return df