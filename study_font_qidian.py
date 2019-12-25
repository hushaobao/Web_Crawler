#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/12/25 9:17
# @Author : hushaobao
# @File   : study_qidian.py
"""
    字体反爬示例
"""


import requests
from fake_useragent import UserAgent
from fontTools.ttLib import TTFont
import os
import re


def get_html(url):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return


def get_num():
    url = 'https://book.qidian.com/info/1011454545'
    html = get_html(url)
    pat1 = '<p><em><style>.*?class="(.*?)">.*?</span></em><cite>'
    font_class = re.findall(pat1, html, re.S)
    pat2 = '<p><em><style>.*?class=".*?">(.*?)</span></em><cite>'
    text = re.findall(pat2, html, re.S)
    font = get_font(font_class)

    print(jiexi(text, font))


def get_font(font_type):
    path = os.path.dirname(os.path.realpath(__file__))

    font_url = "https://qidian.gtimg.com/qd_anti_spider/%s.woff" % font_type[0]
    woff = requests.get(font_url).content
    with open(path + '/fonts.woff', 'wb') as f:
        f.write(woff)
    online_fonts = TTFont(path + '/fonts.woff')
    online_fonts.saveXML("text.xml")
    _dict = online_fonts.getBestCmap()
    return _dict


def jiexi(text, _dict):
    _dic = {
        "six": "6",
        "three": "3",
        "period": ".",
        "eight": "8",
        "zero": "0",
        "five": "5",
        "nine": "9",
        "four": "4",
        "seven": '7',
        "one": "1",
        "two": "2"
    }
    from IPython import embed
    _df = []

    text_ = text[0].replace('&#', '').split(';')
    text_.remove('')
    # embed()
    for inf in text_:
        embed()
        res = _dict.get(int(inf))
        _df.append(_dic[res])
    embed()
    return "".join(_df)


if __name__ == '__main__':
    get_num()
