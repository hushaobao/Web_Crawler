#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/12/19 9:39
# @Author : hushaobao
# @File   : study_multiprocessing_2.py


import requests
import time
from lxml import etree
from multiprocessing import Pool


def run_task(url):
    html = get_html(url)
    get_infos(html)
    time.sleep(1)


def get_html(url):
    '''
    获得 HTML
    '''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/53\
        7.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return


def get_infos(html):
    '''
    提取数据
    '''
    # 解析 html
    html = etree.HTML(html)
    # 提取这一页的满足条件的标签
    infos = html.xpath('//tr[@class="item"]')
    # 循环每一个子标签，提取数据
    for info in infos:
        # 书名
        name = info.xpath('./td[2]/div[1]/a/text()')[0]
        # 作者，出版社，出版时间，价格
        publish_info = info.xpath('./td[2]/p[1]/text()')[0]
        # 评分
        score = info.xpath('./td[2]/div[2]/span[2]/text()')[0]
        # 评价人数
        comment_count = info.xpath('./td[2]/div[2]/span[3]/text()')[0]

        data = {
            '书名': name.replace('\n', '').replace(' ', ''),
            '出版信息': publish_info,
            '评分': score,
            '评价人数': comment_count.replace(' ', '').replace('\n', ''),
        }
        print(data)


def main():
    '''
        主接口
    '''
    urls = ['https://book.douban.com/top250?start={}'
            .format(str(i)) for i in range(0, 226, 25)]
    p = Pool()
    for url in urls:
        p.apply_async(run_task, args=(url,))
    p.close()
    p.join()


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start)
