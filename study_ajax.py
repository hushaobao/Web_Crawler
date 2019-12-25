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
            'Cookie' : 'bid=SWDKJA53JzM; __utmc=30149280; __utmz=30149280.1574666835.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ll="118221"; __utmc=223695111; __yadk_uid=nK6qLsuU4JajFXAX1JSzSo5ltfGaqwbx; _vwo_uuid_v2=D701A2A469A5F1FAF01AE8C2A815EF444|0f6557499082e4a51f87616cb1a9a437; trc_cookie_storage=taboola%2520global%253Auser-id%3Da634cea1-b250-4fdf-9986-e64ad70b5a64-tuct2c948dc; ps=y; push_noty_num=0; push_doumail_num=0; __utmv=30149280.20736; __utma=30149280.1869601630.1574666835.1574995694.1575012320.3; __utmt=1; __utmb=30149280.1.10.1575012320; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1575012332%2C%22https%3A%2F%2Fwww.douban.com%2Fmisc%2Fsorry%3Foriginal-url%3Dhttps%253A%252F%252Fmovie.douban.com%252F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.489557806.1574996950.1574996950.1575012332.2; __utmb=223695111.0.10.1575012332; __utmz=223695111.1575012332.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/misc/sorry; ap_v=0,6.0; _pk_id.100001.4cf6=f13fab216820845c.1574996950.2.1575012481.1574998012'
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

