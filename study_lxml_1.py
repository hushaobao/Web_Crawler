#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/11/25 11:04
# @Author : hushaobao
# @File   : study_lxml_1.py

# 爬取中国最好大学排名

from bs4 import BeautifulSoup
import requests
import time
from IPython import embed
from lxml import etree


# urls = ['https://www.kugou.com/yy/rank/home/{}-23784.html?from=rank'.format(str(i))
#         for i in range(1, 24)]
urls = ['http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html']


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
    # html = BeautifulSoup(HTML, 'lxml')
    html = etree.HTML(HTML)
    ls = html.xpath('//tr[@class="alt"]')

    for info in ls:
        # embed()
        # 排名
        rank = info.xpath('./td[1]/text()')[0]
        # 学校名
        name = info.xpath('./td[2]/div/text()')[0]
        # 省份
        province = info.xpath('./td[3]/text()')[0]
        # 总分
        score = info.xpath('./td[4]/text()')[0]

        print({
            '排名' : rank,
            '校名' : name,
            '省份' : province,
            '总分' : score,
        })
