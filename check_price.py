import os
import subprocess
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("STOCKS_API_KEY")

symbol = "LON:REL"

url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"

res = requests.get(url)
res.raise_for_status()

share_price = float(res.json()["Global Quote"]["05. price"])
price_change = res.json()["Global Quote"]["10. change percent"]
trading_day = res.json()["Global Quote"]["07. latest trading day"]

subject = "daily share price change"
message = f"As of {trading_day}, the {symbol} share price has changed by: {price_change}. Your sharesave is current worth £{int((share_price * 364)/100)}"
recipient = os.getenv("EMAIL")

# print(res.json())
print(message)

subprocess.run(
    ["mail", "-s", subject, recipient],
    input=message,
    text=True)