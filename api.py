import requests
from config import base_currency

def get_rates(base_currency: str) -> dict | None:
    url = f"https://v1.apiplugin.io/v1/currency/lvJlsFo0/rates?source={base_currency}"
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        data = response.json()
        return data.get("rates", {})
    except requests.RequestException as e:
        print(f"Couldn't connect to API: {e}")
        return None

