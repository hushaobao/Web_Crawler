#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/12/17 9:25
# @Author : hushaobao
# @File   : study_ip_agent.py
"""
https://www.xicidaili.com/nn/
http://www.66ip.cn/nmtq.php?getnum=1
第一个 需要解析
第二个 可以自定义数量
"""

import requests
from fake_useragent import UserAgent


# 代理服务器
proxyHost = "117.95.214.240"
proxyPort = "9999"

# 代理隧道验证信息
proxyUser = ''
proxyPass = ''

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

headers = {
    'User-agent': UserAgent().random
}


proxy = {
    'http': 'http://193.34.93.221:53805'
}
url = 'http://icanhazip.com/'
response = requests.get(url, headers=headers, proxies=proxy, timeout=None)
ip = response.text.replace('\n', '')
print(ip)
