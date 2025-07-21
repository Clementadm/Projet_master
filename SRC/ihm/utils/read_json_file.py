import json


def read_json_file(file_name: str) -> str:
    with open(file_name, "r", encoding="utf-8") as f:
        output_data = json.load(f)
    return output_data
