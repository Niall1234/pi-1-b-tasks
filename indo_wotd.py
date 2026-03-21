import requests
from bs4 import BeautifulSoup


url = "https://kbbi.web.id/air"


response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

