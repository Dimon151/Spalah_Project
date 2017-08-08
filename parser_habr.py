#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from settings import *
import re
import time
import random
from pprint import pprint

# from anonum_pars import uesr_agent, proxy

# headers = uesr_agent

list_text = []
headers = HEADERS
python_url = "hub/python/"
SEARCH_URL = (DOMEN + python_url)
print(SEARCH_URL)

html = requests.get(SEARCH_URL, headers=headers).text


def rundom_pause():
    time.sleep(random.randint(1, 3))


def last_pages():
    soup = BeautifulSoup(html, "lxml")
    href_last_page = soup.find("a",
                               class_="toggle-menu__item-link toggle-menu__item-link_pagination toggle-menu__item-link_bordered").get(
        "href")
    regex = re.compile(r"/hub/python/page(\d+)")
    n_page = regex.findall(href_last_page)
    last_page = n_page.pop()
    print(last_page)
    return last_page


def main():
    last_page = int(last_pages())

    with open("habr_python.txt", "w+") as file:
        for page in range(1, last_page + 1):
            print("\nСтраница :", page, "\n")
            url = SEARCH_URL + "page" + str(page)
            #print(url)
            html = requests.get(url, headers=headers).text

            soup = BeautifulSoup(html, "lxml")
            for row in soup.find_all("a", class_="post__title_link"):
                print(row)
                link = row.get('href')
                title = row.text.strip()
                text = {
                    "Link": link,
                    "Text": title,
                }
                pprint(text)

                file.write(str(text))
                file.write("\n")
            rundom_pause()


if __name__ == "__main__":
    main()
