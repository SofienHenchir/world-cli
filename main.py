import os

import requests
from dotenv import load_dotenv

load_dotenv()
user_name = input("Enter your name: ")
country_search = input("Enter a country name: ")
url = os.getenv("BASE_URL") + country_search
headers = {"X-Api-Key": os.getenv("API_Key")}
response = requests.get(url, headers=headers)
print(
    f"{user_name} is looking for informations about {country_search}.. Fetching data .."
)
print(response.json())
