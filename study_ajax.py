#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/11/29 11:12
# @Author : hushaobao
# @File   : study_ajax_2.py
# 爬取豆瓣影评


# https://movie.douban.com/subject/26263417/comments?start=60&limit=20&sort=new_score&status=P
# https://movie.douban.com/subject/26263417/comments?start=40&limit=20&sort=new_score&status=P
# https://movie.douban.com/subject/26263417/comments?start=0&limit=20&sort=new_score&status=P

import requests
import re
from lxml import etree
from fake_useragent import UserAgent


def get_html(url):
    '''
    请求网页
    :param url:
    :return:
    '''
    count = 0 # 计数请求了几次
    while True:
        headers = {
            'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'Cookie' : ''
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response
        else:
            count += 1
            if count == 2:
                return
            continue


def get_comments(response):
    '''
    提取评论
    :param response:
    :return:
    '''

    comments = re.findall(r'class=\\"short\\">(.*?)</span>', response.text, re.S)
    for comment in comments:
        try:
            print(eval(u"'" + comment + "'"))
            print('\n')
        except:
            pass
    pass


if __name__ == '__main__':
    from IPython import embed
    urls = ['https://movie.douban.com/subject/26235346/comments?start={}&amp;limit=20&amp;sort=new_score&amp;status=P&amp;comments_only=1'
            .format(str(i)) for i in range(0,6001,20)]
    for url in urls:
        response = get_html(url)
        # embed()
        get_comments(response)
        pass

