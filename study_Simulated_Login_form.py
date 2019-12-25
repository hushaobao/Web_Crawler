#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/12/16 20:26
# @Author : hushaobao
# @File   : study_Simulated_Login_form.py


import requests
from fake_useragent import UserAgent

url = 'https://accounts.douban.com/j/mobile/login/basic'
headers = {
    'User-agent': UserAgent().random,
}
data = {
    'name': '17854256510',
    'password': 'hushao960815s'
}
response = requests.post(url, headers=headers, data=data)
response.encoding = 'utf-8'
print(response.text)

