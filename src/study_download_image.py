#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/12/18 15:36
# @Author : hushaobao
# @File   : study_download_image.py

import os
import pandas as pd
from tqdm import tqdm
from time import sleep
from multiprocessing import Pool

from utils import down_image_from_url


def download_music163_image(csv_path, save_dir):

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    avatarUrls = pd.read_csv(csv_path, usecols=["avatarUrl"])
    Ids = pd.read_csv(csv_path, usecols=["userId"])
    avatarurls = avatarUrls.values
    ids = Ids.values

    p = Pool(8)
    for idx in tqdm(range(len(avatarurls))):
        url = avatarurls[idx][0]
        save_path = os.path.join(save_dir, f"{ids[idx][0]}.jpg")
        if url == "None":
            continue
        p.apply_async(down_image_from_url, args=(url, save_path))
        sleep(0.05)

    p.close()
    p.join()


if __name__ == "__main__":
    csv_path = "data/music163_28403111.csv"
    save_dir = "data/images_28403111"
    download_music163_image(csv_path, save_dir)
