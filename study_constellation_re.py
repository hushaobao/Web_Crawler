#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/12/17 9:16
# @Author : hushaobao
# @File   : study_constellation_re.py



import requests
import time
import re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


cont = ['Aries', 'Taurus', 'Gemini', 'Cancer',
        'Leo', 'Virgo', 'Libra', 'Scorpio',
        'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
urls = ['https://www.d1xz.net/astro/{}/'.format(i) for i in cont]

headers = {
    'User-agent': UserAgent().random
}


def get_infos(response):
    html = response.text
    pat1 = '<span class="fb st">(.*?)</span>'
    name = re.findall(pat1, html, re.S)[0]
    pat2 = '<p class="txt">(.*?)</p>'
    luck = re.findall(pat2, html, re.S)[1]

    return name.strip(), luck.strip()


def get_html(url):
    count = 0
    while True:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response
        else:
            count += 1
            if count == 3:
                return
            else:
                continue

if __name__ == '__main__':
    f = open('study_constellation_re_res.txt', 'w', encoding='utf-8')
    for url in urls:
        response = get_html(url)
        if response is None:
            continue
        name, luck = get_infos(response)
        f.write(name)
        f.write('\n')
        f.write(luck)
        f.write('\n')
        time.sleep(1)
    f.close()
