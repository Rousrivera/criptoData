import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("x_cg_demo_api_key")
# url = "https://api.coingecko.com/api/v3/simple/price"
url = "https://api.coingecko.com/api/v3/coins/markets"
headers = {
    "x_cg_demo_api_key": api_key,
    "Content-Type": "application/json",
    "Accept": "application/json",
}
# respuesta = requests.get(
#     url=url,
#     headers=headers,
#     params={
#         "vs_currency": "usd",
#         "ids": "bitcoin",
#         "names": "Bitcoin",
#         "symbols": "btc",
#     },
# )

respuesta = requests.get(url=url, headers=headers, params={"vs_currency": "usd"})

print(respuesta.status_code)
# print(respuesta.text)
data = respuesta.json()
print(len(data))
print(data[1]["current_price"])
