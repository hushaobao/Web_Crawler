#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/11/25 15:28
# @Author : hushaobao
# @File   : study_lxml_2.py

# 爬取豆瓣图书TOP250


from bs4 import BeautifulSoup
import requests
import time
from IPython import embed
from lxml import etree


urls = ['https://book.douban.com/top250?start={}'.format(str(i*25))
        for i in range(0, 250//25)]


def get_html(url):
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
               '537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return

for url in urls:
    HTML = get_html(url)
    html = etree.HTML(HTML)
    ls = html.xpath('//tr[@class="item"]')

    for info in ls:
        ch_name = info.xpath('./td[2]/div[1]/a/text()')[0].replace('\n', '').replace(' ', '')
        try:
            en_name = info.xpath('./td[2]/div[1]/span/text()')[0]
        except:
            en_name = 'None'
        pub_info = info.xpath('./td[2]/p[1]/text()')[0]
        score = info.xpath('./td[2]/div[2]/span[2]/text()')[0]
        score_num = info.xpath('./td[2]/div[2]/span[3]/text()')[0].replace('\n', '').replace(' ', '')
        # embed()
        print({
             'name': ch_name,
             'en_name': en_name,
             '出版信息': pub_info,
             '评分': score,
             '评分人数': score_num
             })
