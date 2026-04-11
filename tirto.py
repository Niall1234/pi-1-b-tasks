#!/usr/bin/python3

import feedparser

def rss():
    limit = 3
    text = ""

    rss = feedparser.parse("https://tirto.id/sitemap/r/google-discover")

    feed = rss.feed

    entries = rss.entries

    text += "TIRTO LATEST\n\n"
    for i in range(limit):
        text += entries[i].title + "\n"
        text += entries[i].summary + "\n"
        text += entries[i].link + "\n\n"

    return text