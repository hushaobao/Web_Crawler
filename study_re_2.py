#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/11/25 16:32
# @Author : hushaobao
# @File   : study_re_2.py
# 获取成时GDP人口


import re
import requests
import time


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


url = 'http://caifuhao.eastmoney.com/news/20190201115604564011000'
pat = '<p>(\d+.*?)</p>|<p><strong>(\d+.*?)</p>'
# '<p>(\d+.*?)</p>' |
html = get_html(url)
infos = re.findall(pat, html, re.S)

data = []
for info in infos[1:]:
    pat1 = r'(\d+?)亿元'
    GDP = re.findall(pat1, info[0])
    pat2 = r'人口：(\d*)）'
    people_num = re.findall(pat2, info[0])
    pat3 = r'\.(.*?)\d+?亿元'
    city = re.findall(pat3, info[0])
    print({
        'city ': city,
        'people_num ': people_num,
        'GDP ': GDP
    })
