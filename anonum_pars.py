#!/usr/bin/env python3

import random
from pprint import pprint
import os
import sqlite3

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0"
}

UPDATE = True

USER_AGENT_BASE = os.path.abspath("user_agent_list.base")

USER_AGENT_BD = os.path.abspath("useragents.bd")

uesr_agent_list = []


def get_ua(UPDATE, USER_AGENT_BD):
    if UPDATE == True:
        conn = sqlite3.connect(USER_AGENT_BD)
        #p = open(USER_AGENT_BASE, "w+", encoding='utf-8')
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS useragents")
        c.execute('''CREATE TABLE IF NOT EXISTS useragents
                      (id int auto_increment primary key,
                                   useragent TEXT(250))''')

        uesr_agent_list = (requests.get('https://whichbrowser.net/data/useragents.txt',
                                        headers=HEADERS).text).split("\n")
        #pprint(uesr_agent_list)

        for i in uesr_agent_list:
            # print(i)
            # print(type(i))
            #p.write(i)
            c.execute("INSERT INTO useragents (useragent) VALUES (?)", (i,))
            conn.commit()
            print("Commit END")
        # i = "test"
        # c.execute("INSERT INTO useragents (useragent) VALUES (?)", (i,))
        # conn.commit()


        c.close()
        conn.close()
        print("Write END")

    else:
        # p = open(USER_AGENT_BASE, "r", encoding='utf-8')
        # p.read(uesr_agent_list)
        conn = sqlite3.connect("useragents.bd")
        c = conn.cursor()
        c.execute("SELECT * FROM useragents ORDER BY RANDOM() LIMIT 1")
        uesr_agent_list = c.fetchall()

    uesr_agent = {
        "user-agent": random.choice(uesr_agent_list)
    }
    return uesr_agent


tr_teg = []

uesr_agent = get_ua(UPDATE, USER_AGENT_BD)

proxy_list = []


def get_proxy():
    proxy_html = requests.get('https://premproxy.com/list/', headers=uesr_agent).text
    soup = BeautifulSoup(proxy_html, "lxml")
    proxy_list = [row.find('td').text for row in soup.find_all('tr', class_="anon")]
    proxy = {
        'https': 'https://' + random.choice(proxy_list)
    }
    return proxy


# def get_proxy():
#     proxy_html = requests.get('https://premproxy.com/list/', headers=uesr_agent).text
#     soup = BeautifulSoup(proxy_html, "lxml")
#
#     proxy_list = [row.find('td').text for row in soup.find_all('tr', class_="anon")]
#
#     proxy = {
#         'https': 'https://' + random.choice(proxy_list)
#     }
#     return proxy



proxy = get_proxy()


# print("\nusr_agnt :", uesr_agent)
# print("proxy :", proxy)


def main():
    print("\nusr_agnt :", uesr_agent)

    proxy = get_proxy()
    print("proxy :", proxy)

    get_my_ip = requests.get("https://whoer.net/ru", params=None, headers=uesr_agent, proxies=proxy).text
    soup_ip = BeautifulSoup(get_my_ip, "lxml")

    my_ip = soup_ip.find('strong').text.strip()
    print("My IP: ", my_ip)

    my_loc = soup_ip.find("dd").text.strip()
    print("My location: ", my_loc)

    my_ua = soup_ip.find('span', class_="cont browser-ua-headers").text.strip()
    print("My USER-AGENT: ", my_ua)


if __name__ == "__main__":
    main()
