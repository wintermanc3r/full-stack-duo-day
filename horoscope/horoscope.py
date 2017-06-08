#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

sign = input("What's your sign? ")
r = requests.get("https://www.astrology.com/horoscope/daily/{}.html"
                 .format(sign))
if r.status_code != 200:
    print("Unknown sign.")
    exit()
soup = BeautifulSoup(r.text, 'lxml')
horoscope = soup.find("div", class_="page-horoscope-text")
print(horoscope.get_text())
