from get_word import get_word
from indonesian_news import get_news

# setting roundup email variables

message = """"""

message += get_news()

message += get_word()

print(message)