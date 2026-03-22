import requests
from bs4 import BeautifulSoup


url = "https://kbbi.web.id/"


response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
tags = soup.find_all("div", class_="col")
for tag in tags:
    links = soup.find_all("a")
    for link in links:
        if "./" in link.get("href"):
            print(link.get("href"))