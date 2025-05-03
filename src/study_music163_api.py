#!/usr/bin/python
# -*- coding:utf-8 -*-
# doc: docs/cloud_music163.md


import os
import csv
import json
import time

from tqdm import tqdm
from utils import get_url


def timestamp2strftime(timestamp):
    """timestamp-ms convert strftime("%Y-%m-%d %H:%M:%S")

    Args:
        timestamp (float): _description_

    Returns:
        str: str format time
    """
    struct_time = time.localtime(timestamp / 1000.0)
    strftime = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
    return strftime


def get_comment_music163(music_id, save_dir="data/"):
    """get comment from music163 by music id
    Args:
        muscic_id (str): cloud music id

    Returns:
        list: comment list
    """

    limit = 50
    num_max_comment = 5000
    time_sleep = 0.5

    urls = [
        f"http://music.163.com/api/v1/resource/comments/R_SO_4_{music_id}?limit={limit}&offset={i}"
        for i in range(0, num_max_comment, limit)
    ]

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    save_path = os.path.join(save_dir, "music163_" + music_id + ".csv")

    f = open(save_path, "w", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)

    # write header
    writer.writerow(
        ["userId", "nickname", "avatarUrl", "content", "likedCount", "time"]
    )

    for url in tqdm(urls):
        response_text = get_url(url)
        json_data = json.loads(response_text)

        hotComments = json_data.get("hotComments", [])
        comments = json_data.get("comments", [])
        comments = hotComments + comments

        for hot_com in comments:
            # user info
            user = hot_com["user"]
            userId = user.get("userId", "None")
            avatarUrl = user.get("avatarUrl", "None")
            nickname = user.get("nickname", "None")

            # comment info
            content = hot_com.get("content", "").replace("\n", "").replace(" ", "")
            time_ms = hot_com.get("time", "None")
            likedCount = hot_com.get("likedCount", "None")
            time_str = timestamp2strftime(time_ms)

            # write to csv
            writer.writerow(
                [userId, nickname, avatarUrl, content, likedCount, time_str]
            )
        time.sleep(time_sleep)

    f.close()


if __name__ == "__main__":
    music_id = "28403111"
    get_comment_music163(music_id)
