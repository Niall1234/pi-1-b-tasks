import os
import subprocess
import requests
import pprint as pp
from dotenv import load_dotenv

load_dotenv()

CODE = "RELX"
API_KEY = os.getenv("STOCKS_API_KEY")
ENDPOINT = os.getenv("ENDPOINT")

intel_url = f"{ENDPOINT}query?function=GLOBAL_QUOTE&symbol={CODE}&apikey={API_KEY}"

res = requests.get(intel_url)
res.raise_for_status()

data = pp.pformat(res.json())

# print(data)

message = data
subject = f"{CODE} - Share value"
recipient = os.getenv("EMAIL")

subprocess.run(
    ["mail", "-s", subject, recipient],
    input=message,
    text=True
)