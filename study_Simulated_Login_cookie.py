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
    'Cookie': ''
}
response = requests.get(url, headers=headers)

response.encoding = 'utf-8'
tmp = response.text
print(response.text)
