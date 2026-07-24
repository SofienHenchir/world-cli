import os

import pandas as pd
import requests
from dotenv import load_dotenv


def main():
    print("Welcome to World CLI!")
    load_dotenv()

    user_name = input("Enter your name: ")
    country_search = input("Enter a country name: ")
    url = os.getenv("BASE_URL") + country_search
    headers = {"X-Api-Key": os.getenv("API_Key")}
    response = requests.get(url, headers=headers)
    print(
        f"{user_name} is looking for informations aboutt {country_search}.. Fetching data .."
    )
    result = response.json()

    if isinstance(result, list) or isinstance(result, dict):  # noqa: SIM101
        df = pd.json_normalize(result)
    else:
        df = pd.DataFrame({"result": [result]})

    print(df)
