#!/usr/bin/python3

import os
import subprocess
from get_word import get_word
from indonesian_news import get_news
from tirto import rss

# setting roundup email variables

message = ""

message += get_news()

message += get_word()

message += rss()

subject = "Indonesian Daily Digest"
recipient = os.getenv("EMAIL")

subprocess.run(
    ["mail", "-s", subject, recipient],
    input=message,
    text=True
)
