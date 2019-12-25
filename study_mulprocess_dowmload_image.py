#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/12/19 9:56
# @Author : hushaobao
# @File   : study_mulprocess_dowmload_image.py

"""
    download music 163 Personal information images
"""

import csv
import pandas as pd
import os
import time
from IPython import embed
from multiprocessing import Pool
import requests
from fake_useragent import UserAgent


def down_image(url, name):

    save_path = 'music_163_images/28461702/' + str(name) + '_' + url.split('/')[-1]
    try:
        if not os.path.exists(save_path):
            response = requests.get(url, headers={'User-agent': UserAgent().random})
            with open(save_path, 'wb') as f:
                f.write(response.content)
                print('idx-{} done...'.format(url.split('/')[-1]), os.getpid())
        else:
            print('idx-{} exist...'.format(url.split('/')[-1]))
    except:
        print(url)
        embed()

if __name__ == '__main__':
    file_path = 'music_163_api_28461702.csv'
    avatarUrls = pd.read_csv(file_path, usecols=['avatarUrl'])
    Ids = pd.read_csv(file_path, usecols=['userId'])
    avatarurls = avatarUrls.values
    ids = Ids.values
    # embed()
    p = Pool(4)   # 参数就是进程数。默认为None，进程数为os.cpu_count() cpu的个数，并交给进程池。
    for idx in range(len(avatarurls)):
        # embed()
        if avatarurls[idx][0] == 'None':
            continue
        # 进程池中同步提交任务的方法，没有并发效果，提交完1个后自带join方法，等着上一个任务结束。
        p.apply(down_image, args=(avatarurls[idx][0], ids[idx][0]))
