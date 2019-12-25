#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/11/25 16:05
# @Author : hushaobao
# @File   : study_re_1.py

# 爬取斗破苍穹标题

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


# \d+：由于我们看到 每次 href 属性不同，所以需要匹配，\d 匹配一个数字，+ 匹配多个数字
# .*?：匹配尽可能多的满足的字符，也叫贪婪匹配，我们这里标题是字符串，所以用它，当然也可以用它替换上面的 \d+
pat = '<dd> <a style="" href="/book/390/\d+.html">(.*?)</a></dd>'

url = 'https://www.qu.la/book/390/'
html = get_html(url)

# re.S：是一种匹配的模式，是指允许换行匹配
titles = re.findall(pat, html, re.S)
for info in titles[0:20]:
    print(info)
