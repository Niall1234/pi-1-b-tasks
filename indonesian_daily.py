import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# setting roundup email variables
text = """"""



# news API 
TOKEN = os.getenv("NEWS_API_KEY")

country = "id"

url = "https://api.thenewsapi.com/v1/news/top"

params = {
    "api_token": TOKEN,
    "language": country,
    "limit": "3",
    "locale": country,
    "published_on": datetime.now().strftime('%Y-%m-%d')
}

response_json = requests.get(url, params=params).json()

text += "NEWS\n\n"
for object in response_json["data"]:
    text += f"Title: {object["title"]}\n"
    text += f"Desc: {object["description"]}\n"
    text += f"URL: {object["url"]}\n"
    text += f"Published at: {object["published_at"]}\n\n"

print(text)
