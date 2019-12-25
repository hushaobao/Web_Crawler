#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/12/16 21:19
# @Author : hushaobao
# @File   : study_constellation_css.py

"""
    验证写的 css，xpath 表达式是否正确 --- Console验证
    css 验证: 输入 $(), 括号中写 css 表达式, 如果正确那么就会有如图所示的显示提取结果, 不正确那就没有结果
    
    xpath 验证：输入 $x()
    
    用此方法, 可以方便的先验证表达式是否正确, 再填入代码中
"""
import requests
import time
import cssselect
from lxml import etree
from fake_useragent import UserAgent


cont = ['Aries', 'Taurus', 'Gemini', 'Cancer',
        'Leo', 'Virgo', 'Libra', 'Scorpio',
        'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
urls = ['https://www.d1xz.net/astro/{}/'.format(i) for i in cont]

headers = {
    'User-agent': UserAgent().random
}


def get_infos(response):
    html = etree.HTML(response.text)
    luck = html.cssselect('.xz_det.fr > p.txt')[0].text
    name = html.cssselect('.xz_det.fr > p.words > span.fb.st')[0].text
    return name.strip(), luck.strip()


def get_html(url):
    count = 0
    while True:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response
        else:
            count += 1
            if count == 3:
                return
            else:
                continue

if __name__ == '__main__':
    f = open('study_constellation_css_res.txt', 'w', encoding='utf-8')
    for url in urls:
        response = get_html(url)
        if response is None:
            continue
        name, luck = get_infos(response)
        f.write(name)
        f.write('\n')
        f.write(luck)
        f.write('\n')
    f.close()
