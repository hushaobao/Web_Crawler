#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/11/29 15:06
# @Author : hushaobao
# @File   : study_csv.py

import requests
import re
import time
import csv
from fake_useragent import UserAgent


urls = ['https://www.mcdonalds.com.cn/index/Quality/publicinfo/deliveryinfo?_ga=0&page={}'
        .format(str(i)) for i in range(1, 243)]


def get_html(url):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return


def info(html):
    pat1 = '<span>城市</span>(.*?)</td>'
    cities = [i.replace(' ', '') for i in re.findall(pat1, html, re.S)]

    pat2 = '<span>门店编号</span>(.*?)</td>'
    number = [i.replace(' ', '') for i in re.findall(pat2, html, re.S)]

    pat3 = '<span>门店名称</span>(.*?)</td>'
    shop_names = [i.replace(' ', '') for i in re.findall(pat3, html, re.S)]
    infos = zip(cities, number, shop_names)
    # from IPython import embed
    # embed()
    return infos


if __name__ == "__main__":
    with open('output.csv', 'w', encoding='utf-8', newline='') as f:
        # 创建写入对象
        writer = csv.writer(f)
        # 写入第一行头信息
        writer.writerow(['city', 'number', 'shop_name'])

        for url in urls:
            html = get_html(url)
            infos = info(html)
            for inf in infos:
                writer.writerow(inf)

