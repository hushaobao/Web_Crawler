#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/12/16 22:08
# @Author : hushaobao
# @File   : study_constellation_xpath.py


from lxml import etree
import requests
import time
from lxml import etree
from fake_useragent import UserAgent



cont = ['Aries', 'Taurus', 'Gemini', 'Cancer',
        'Leo', 'Virgo', 'Libra', 'Scorpio',
        'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
urls = ['https://www.d1xz.net/astro/{}/'.format(i) for i in cont]

headers = {
    'User-agent': UserAgent().random
}


def get_infos(response):
    html = etree.HTML(response.text)
    luck = html.xpath('//p[@class="txt"]/text()')[0]
    name = html.xpath('//p[@class="t"]/text()')[0]
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
    f = open('study_constellation_xpath_res.txt', 'w', encoding='utf-8')
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
