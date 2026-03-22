import json
import requests
from bs4 import BeautifulSoup

kamus = {
    "index": "https://kbbi.web.id",
    "word_links": []
}

response = requests.get(kamus["index"])
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
tags = soup.find_all("div", class_="col")
for tag in tags:
    links = soup.find_all("a")
    for link in links:
        if "./" in link.get("href"):
            kamus["word_links"].append(link.get("href")[1:])

with open("kamus.json", "w") as json_file:
    json.dump(kamus, json_file)