import requests
import pandas as pd

def get_crypto_data(coin="bitcoin"):

    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"

    params = {
        "vs_currency": "usd",
        "days": "365"
    }

    response = requests.get(url, params=params)

    data = response.json()

    # Debug print (optional)
    # print(data)

    if "prices" not in data:
        raise Exception("API Error: 'prices' data not found. Response: " + str(data))

    prices = data["prices"]

    df = pd.DataFrame(prices, columns=["timestamp", "price"])

    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")

    df = df[["date", "price"]]

    return df
