#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/11/22 17:02
# @Author : hushaobao
# @File   : study.py

# 爬取酷狗音乐热门歌曲信息top500


from bs4 import BeautifulSoup
import requests
import time
from IPython import embed


urls = ['https://www.kugou.com/yy/rank/home/{}-23784.html?from=rank'.format(str(i))
        for i in range(1, 24)]


def get_html(url):
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
               '537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return

for url in urls:
    HTML = get_html(url)
    html = BeautifulSoup(HTML, 'lxml')
    # ranks = html.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num')
    # names = html.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
    # times = html.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')
    ranks = html.find_all('span', class_='pc_temp_num')
    names = html.find_all('a', class_='pc_temp_songname')
    times = html.find_all('span', class_='pc_temp_time')

    for r, n, t in zip(ranks, names, times):
        embed()
        r = r.get_text().replace('\n', '').replace('\t', '').replace('\r', '')
        n = n.get_text()
        t = t.get_text().replace('\n', '').replace('\t', '').replace('\r', '')
        data = {
            '排名': r,
            '歌名-歌手': n,
            '播放时间': t
        }
        print(data)
