# -*- coding:utf-8 -*-
import requests
from pyquery import PyQuery as pq
from _file import *
def main():
    url = "https://home.unicode.org/emoji/emoji-frequency/"
    response = requests.get(url)
    doc = pq(response.text)
    items = doc("tbody tr td").items()
    emojis = []
    for item in items:
        emojis.append(item.text())
    writeToFile("unicode.json",emojis,encoding="UTF-16")
if __name__ == "__main__":
    main()