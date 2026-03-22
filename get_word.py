import json
import random
import requests
from bs4 import BeautifulSoup

def get_word():

    with open("kamus.json", mode="r", encoding="utf-8") as read_json_file:
        kamus = json.load(read_json_file)

    random_word_url = kamus["index"] + random.choice(kamus["word_links"])

    response = requests.get(random_word_url)
    response.raise_for_status()

    print(random_word_url)
    soup = BeautifulSoup(response.text, "html.parser")
    container = soup.find("div", id="d1")
    for element in container:
        print(element)

