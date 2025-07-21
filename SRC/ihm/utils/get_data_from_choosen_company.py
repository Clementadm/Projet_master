import os
from datetime import datetime
from typing import Dict


def extract_date_filename(file_name: str) -> datetime:
    """
    Extract the date from a file name in the format 'prefix_data_YYYY_MM_DD.json'
    and return it as a datetime object.

    Parameters:
        file_name (str): The name of the file (e.g. 'wmt_data_2025_07_17.json').

    Returns:
        datetime: A datetime object representing the extracted date.
    """
    get_date_from_file_name = file_name.split("_data_")[-1].replace(".json", "")
    datetime_filename = datetime.strptime(get_date_from_file_name, "%Y_%m_%d")
    return datetime_filename


def get_data_of_choosen_company(
    company_dict: Dict[str, str], choosen_company: str
) -> str:
    """
    Given a dictionary mapping company names to tickers and a chosen company name,
    returns the filename of the most recent data file for that company.

    Input:
        company_dict: Dictionary mapping company names to their ticker symbols.
        choosen_company: The name of the company selected by the user (st.selectbox).

    Output:
        str: The filename of the latest JSON file containing data for the selected company.
    """
    ticker = company_dict[choosen_company]
    folder_path = "data/output/all_data_regroup"
    file_list = os.listdir(folder_path)

    # Get fil only matching with the select company (ticker)
    file_of_choosen_company = [
        filename for filename in file_list if filename.startswith(f"{ticker}_data_")
    ]

    # Filename containing the most recent date
    latest_file = max(file_of_choosen_company, key=extract_date_filename)
    print(f"File use for Dahboard (latest_file): {latest_file}")

    path_latst_file = "data/output/all_data_regroup/" + latest_file
    return path_latst_file


# def get_data_of_choosen_company(company_dict, choosen_company):
#     ticker = company_dict[choosen_company]
#     print("ticker: ", ticker)
#     folder_path = "data/output/all_data_regroup"
#     file_list = os.listdir(folder_path)

#     file_of_choosen_company = []
#     for filename in file_list:
#         if filename.split("_")[0] == ticker:
#             file_of_choosen_company.append(filename)

#     latest_file = max(file_of_choosen_company, key=extract_date_filename)
#     print(f"File use for Dahboard (latest_file):{latest_file}")
#     return latest_file
