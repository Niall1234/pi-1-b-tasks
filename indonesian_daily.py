import os
import subprocess
from get_word import get_word
from indonesian_news import get_news

# setting roundup email variables

message = """"""

message += get_news()

message += get_word()

subject = "Indonesian Daily Digest"
recipient = os.getenv("EMAIL")

subprocess.run(
    ["mail", "-s", "subject", "recipient"],
    input=message,
    text=True
)