import json
from binance.client import Client

with open("./keys.json", mode="r", encoding="utf-8") as file:
    binance = json.load(file)

client = Client(api_key=binance["apiKey"], api_secret=binance["secretKey"], tld="us")

client.get_account()
