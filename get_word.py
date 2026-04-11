#!/usr/bin/python3

import os
import json
import random
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

def get_word():

    message = ""

    with open(os.path.join(os.getenv("WORD_FILE_PATH"), "kamus.json"), mode="r", encoding="utf-8") as read_json_file:
        kamus = json.load(read_json_file)

    random_word_url = kamus["index"] + random.choice(kamus["word_links"])

    response = requests.get(random_word_url)
    response.raise_for_status()

    # print(random_word_url)
    soup = BeautifulSoup(response.text, "html.parser")
    container = soup.find("div", id="d1")

    definition = container.text
    for element in container:
        word = soup.find("b").text

    message += "WORD OF THE DAY\n"
    message += f"\n{word}\n"
    message += f"{definition}\n\n"

    return message
