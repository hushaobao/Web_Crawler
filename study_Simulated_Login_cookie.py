#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/12/16 19:58
# @Author : hushaobao
# @File   : study_Simulated_Login_cookie.py

import requests
from fake_useragent import UserAgent

url = 'https://weibo.com/5979786722/follow?rightmod=1&wvr=6'
headers = {
    'User-agent': UserAgent().random ,
    'Cookie': 'SCF=AqzjMCmyp4g5RWmrfwmhCqu48ptqvWNCptza8wnlj3S4LoxZb'
              'eVeuU8LosjucELHFNkJZdMIMK21_4NwEIKir3w.; SUB=_2A25w8z'
              'gMDeRhGeNH7FsW-CjLyT6IHXVTiS7ErDV8PUJbktAfLU_XkW9NSm6H'
              '2Tg_-lSB_1V0XQQuSxQK3Q0egNkA; SUBP=0033WrSXqPxfM725Ws9'
              'jqgMF55529P9D9WWMKpsL06XJf.e9J0NvahUJ5JpX5K2hUgL.Fo-4S0'
              '.N1hqNeoz2dJLoIE5LxK-L12qLBoqLxK-LB-BL1K5LxKBLBonLBo9Kdg'
              'Lj9Btt; SUHB=0u5RFgqQTZWuXH; Ugrow-G0=7e0e6b57abe2c2f76f6'
              '77abd9a9ed65d; wvr=6; YF-V5-G0=9717632f62066ddd544bf04f733'
              'ad50a; _s_tentry=-; Apache=4310461401929.4883.1576498126034'
              '; SINAGLOBAL=4310461401929.4883.1576498126034; ULV=15764981'
              '26094:1:1:1:4310461401929.4883.1576498126034:; wb_view_log_5'
              '979786722=1920*10801%261366*7681; YF-Page-G0=4b5a51adf43e782'
              'f0f0fb9c1ea76df93|1576498339|1576498126; webim_unReadCount=%'
              '7B%22time%22%3A1576498762176%2C%22dm_pub_total%22%3A0%2C%22c'
              'hat_group_client%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D'
}
response = requests.get(url, headers=headers)

response.encoding = 'utf-8'
tmp = response.text
print(response.text)
