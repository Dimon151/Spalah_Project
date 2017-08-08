#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from settings import *
from pprint import pprint
from anonum_pars import uesr_agent, proxy

headers = uesr_agent

list_profils = []


def parse(html):
    soup = BeautifulSoup(html, "lxml")
    for row in soup.find_all('div', class_="up-video-box friend-box nobrd"):
        img = row.find('img').get('src')
        title = row.find('div', class_="inner")
        link = title.find('a').get('href')
        name = title.find('a').text
        age = title.find('span', class_="orange").text.strip()

        data = {
            'Name': name,
            'Age': age,
            'Image': img,
            'Link': DOMEN + link,
        }

        list_profils.append(data)
    return list_profils


def who_is_i():
    get_my_ip = requests.get("https://whoer.net/ru", params=None, headers=uesr_agent, proxies=proxy).text
    soup_ip = BeautifulSoup(get_my_ip, "lxml")

    my_ip = soup_ip.find('strong').text.strip()
    # print("My IP: ", my_ip)

    my_loc = soup_ip.find("dd").text.strip()
    # print("My location: ", my_loc)

    my_ua = soup_ip.find('span', class_="cont browser-ua-headers").text.strip()
    # print("My USER-AGENT: ", my_ua)
    return {
        print("My IP: ", my_ip),
        print("My location: ", my_loc),
        print("My USER-AGENT: ", my_ua)

    }


def main():
    print(headers, "\n", proxy)
    print(who_is_i())
    get_html = requests.get(url=SEARCH_URL, params=payload,
                            headers=headers, proxies=proxy).text
    pprint(parse(get_html))


if __name__ == '__main__':
    main()
