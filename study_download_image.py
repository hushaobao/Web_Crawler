#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/12/18 15:36
# @Author : hushaobao
# @File   : study_download_image.py


import requests
import time
import re
import os
from fake_useragent import UserAgent


def get_html(url):

    headers = {
        'User-agent': UserAgent().random
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return None


def get_infos(html):

    img_urls = re.findall('srcset=".*?1x, (.*?) 2x"', html, re.S)
    conts = re.findall('alt="(.*?)">', html, re.S)
    names = [cont.replace(', ', '_') for cont in conts]
    return img_urls, names


if __name__ == '__main__':
    urls = ['https://pixabay.com/zh/images/search/?pagi={}'.format(str(i))
            for i in range(1, 1001)]
    save_root_path = 'image/'
    if not os.path.exists(save_root_path):  # 判断此路径是否存在，没有，则创建
        os.mkdir(save_root_path)

    for url in urls:
        html = get_html(url)
        if html is None:
            continue
        img_urls, names = get_infos(html)
        for idx in range(len(img_urls)):

            save_path = save_root_path + names[idx] + '.jpg'

            if not os.path.exists(save_path):
                response = requests.get(img_urls[idx], headers={'User-agent': UserAgent().random})
                with open(save_path, 'wb') as f:
                    f.write(response.content)
                    print('idx-{} done...'.format(idx))
            else:
                print('图片存在')
    # print()
    time.sleep(1)
