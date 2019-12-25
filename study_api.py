#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/12/17 21:54
# @Author : hushaobao
# @File   : study_api.py

"""
https://mp.weixin.qq.com/s/ZxqRmTVKTcunMw023m5wug

1、网易云音乐评论 api 接口 --- 其中的歌曲 id 记得替换，id 在 url 可以看到的：
    http://music.163.com/api/v1/resource/comments/R_SO_4_{歌曲ID}?limit=20&offset=0
        limit：返回数据条数(每页获取的数量)，默认为20，可以自行更改
        offset：偏移量(翻页)，offset需要是limit的倍数
        type：搜索的类型
    举例，比如limit设置为10，则第一页，第二页分别为：
    http://music.163.com/api/v1/resource/comments/R_SO_4_483671599?limit=10&offset=0
    http://music.163.com/api/v1/resource/comments/R_SO_4_483671599?limit=10&offset=10
    返回的数据格式为 json，就是 python 中的字典，需要注意的是通过此接口获取的评论数量最多2万条。
2、个人信息api 接口：
    https://music.163.com/api/v1/user/detail/{用户ID}
3、歌词api接口
    https://music.163.com/api/song/lyric?id={歌曲ID}&lv=1&kv=1&tv=-1
4、歌单api
    https://music.163.com/api/playlist/detail?id={歌单ID}
    id=19723756，云音乐飙升榜
    id=3779629，云音乐新歌榜
    id=3778678，云音乐热歌榜
    id=2250011882，抖音排行榜
5、搜索
    http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={搜索内容}&type=1&offset=0&total=true&limit=20
    参数：
        limit：返回数据条数（每页获取的数量），默认为20，可以自行更改
        
        offset：偏移量（翻页），offset需要是limit的倍数
        type：搜索的类型
            type=1           单曲
            type=10         专辑
            type=100        歌手
            type=1000      歌单
            type=1002      用户
            type=1004      MV
            type=1006      歌词
            type=1009      主播电台
6、其他
    歌手专辑
    http://music.163.com/api/artist/albums/{歌手ID}?id={歌手ID}&offset=0&total=true&limit=10
    
    专辑信息
    http://music.163.com/api/album/{专辑ID}?ext=true&id={专辑ID}&offset=0&total=true&limit=10
    
    歌曲信息
    http://music.163.com/api/song/detail/?id={歌曲ID}&ids=%5B{歌曲ID}%5D
    
    MV
    http://music.163.com/api/mv/detail?id={MV的ID}&type=mp4
"""


import time
import csv
import requests
import json
import jsonpath
from IPython import embed


def ms2tm(ms):
    """
    将时间戳转换成时间
    :param ms: 以毫秒为单位的时间戳
    :return: 格式化时间
    """
    # print(ms, type(float(ms)/1000))
    data_sj = time.localtime(float(ms)/1000)
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", data_sj)  # 时间戳转换正常时间
    return time_str


music_id = '28461702'
# url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_513360721?limit=20&offset=0'
urls = ['http://music.163.com/api/v1/resource/comments/R_SO_4_{}?limit=50&offset={}'
        .format(music_id, str(i)) for i in range(0, 5050, 50)]

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}

save_csv_path = 'music_163_api_' + music_id + '.csv'
f = open(save_csv_path, 'w', encoding='utf-8', newline='')
writer = csv.writer(f)
# 写入第一行头信息
writer.writerow(['userId', 'nickname', 'avatarUrl', 'content', 'likedCount', 'time'])

for url in urls:
    response = requests.get(url, headers=headers)
    json_txt = json.loads(response.text)
    hotComments = json_txt.get('hotComments', 0)
    if hotComments != 0:
        for hot_com in hotComments:
            # embed()
            user = hot_com['user']
            userId = user.get('userId', 'None')
            avatarUrl = user.get('avatarUrl', 'None')
            nickname = user.get('nickname', 'None')
            content = hot_com.get('content', 'None')
            time_ms = hot_com.get('time', 'None')
            likedCount = hot_com.get('likedCount', 'None')
            time_str = ms2tm(time_ms)
            writer.writerow((userId, nickname, avatarUrl, content, likedCount, time_str))
    for hot_com in json_txt['comments']:
        user = hot_com['user']
        userId = user.get('userId', 'None')
        avatarUrl = user.get('avatarUrl', 'None')
        nickname = user.get('nickname', 'None')
        content = hot_com.get('content', 'None')
        likedCount = hot_com.get('likedCount', 'None')
        time_ms = hot_com.get('time', 'None')
        time_str = ms2tm(time_ms)
        writer.writerow((userId, nickname, avatarUrl, content, likedCount, time_str))
    time.sleep(1)
    # from IPython import embed
    # embed()
    # names = jsonpath.jsonpath(json_txt, '$..content')
    # for name in names:
    #     print(name)

f.close()
#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/12/17 21:54
# @Author : hushaobao
# @File   : study_api.py

"""
https://mp.weixin.qq.com/s/ZxqRmTVKTcunMw023m5wug

1、网易云音乐评论 api 接口 --- 其中的歌曲 id 记得替换，id 在 url 可以看到的：
    http://music.163.com/api/v1/resource/comments/R_SO_4_{歌曲ID}?limit=20&offset=0
        limit：返回数据条数(每页获取的数量)，默认为20，可以自行更改
        offset：偏移量(翻页)，offset需要是limit的倍数
        type：搜索的类型
    举例，比如limit设置为10，则第一页，第二页分别为：
    http://music.163.com/api/v1/resource/comments/R_SO_4_483671599?limit=10&offset=0
    http://music.163.com/api/v1/resource/comments/R_SO_4_483671599?limit=10&offset=10
    返回的数据格式为 json，就是 python 中的字典，需要注意的是通过此接口获取的评论数量最多2万条。
2、个人信息api 接口：
    https://music.163.com/api/v1/user/detail/{用户ID}
3、歌词api接口
    https://music.163.com/api/song/lyric?id={歌曲ID}&lv=1&kv=1&tv=-1
4、歌单api
    https://music.163.com/api/playlist/detail?id={歌单ID}
    id=19723756，云音乐飙升榜
    id=3779629，云音乐新歌榜
    id=3778678，云音乐热歌榜
    id=2250011882，抖音排行榜
5、搜索
    http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={搜索内容}&type=1&offset=0&total=true&limit=20
    参数：
        limit：返回数据条数（每页获取的数量），默认为20，可以自行更改
        
        offset：偏移量（翻页），offset需要是limit的倍数
        type：搜索的类型
            type=1           单曲
            type=10         专辑
            type=100        歌手
            type=1000      歌单
            type=1002      用户
            type=1004      MV
            type=1006      歌词
            type=1009      主播电台
6、其他
    歌手专辑
    http://music.163.com/api/artist/albums/{歌手ID}?id={歌手ID}&offset=0&total=true&limit=10
    
    专辑信息
    http://music.163.com/api/album/{专辑ID}?ext=true&id={专辑ID}&offset=0&total=true&limit=10
    
    歌曲信息
    http://music.163.com/api/song/detail/?id={歌曲ID}&ids=%5B{歌曲ID}%5D
    
    MV
    http://music.163.com/api/mv/detail?id={MV的ID}&type=mp4
"""


import time
import csv
import requests
import json
import jsonpath
from IPython import embed


def ms2tm(ms):
    """
    将时间戳转换成时间
    :param ms: 以毫秒为单位的时间戳
    :return: 格式化时间
    """
    # print(ms, type(float(ms)/1000))
    data_sj = time.localtime(float(ms)/1000)
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", data_sj)  # 时间戳转换正常时间
    return time_str


music_id = '28461702'
# url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_513360721?limit=20&offset=0'
urls = ['http://music.163.com/api/v1/resource/comments/R_SO_4_{}?limit=50&offset={}'
        .format(music_id, str(i)) for i in range(0, 5050, 50)]

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}

save_csv_path = 'music_163_api_' + music_id + '.csv'
f = open(save_csv_path, 'w', encoding='utf-8', newline='')
writer = csv.writer(f)
# 写入第一行头信息
writer.writerow(['userId', 'nickname', 'avatarUrl', 'content', 'likedCount', 'time'])

for url in urls:
    response = requests.get(url, headers=headers)
    json_txt = json.loads(response.text)
    hotComments = json_txt.get('hotComments', 0)
    if hotComments != 0:
        for hot_com in hotComments:
            # embed()
            user = hot_com['user']
            userId = user.get('userId', 'None')
            avatarUrl = user.get('avatarUrl', 'None')
            nickname = user.get('nickname', 'None')
            content = hot_com.get('content', 'None')
            time_ms = hot_com.get('time', 'None')
            likedCount = hot_com.get('likedCount', 'None')
            time_str = ms2tm(time_ms)
            writer.writerow((userId, nickname, avatarUrl, content, likedCount, time_str))
    for hot_com in json_txt['comments']:
        user = hot_com['user']
        userId = user.get('userId', 'None')
        avatarUrl = user.get('avatarUrl', 'None')
        nickname = user.get('nickname', 'None')
        content = hot_com.get('content', 'None')
        likedCount = hot_com.get('likedCount', 'None')
        time_ms = hot_com.get('time', 'None')
        time_str = ms2tm(time_ms)
        writer.writerow((userId, nickname, avatarUrl, content, likedCount, time_str))
    time.sleep(1)
    # from IPython import embed
    # embed()
    # names = jsonpath.jsonpath(json_txt, '$..content')
    # for name in names:
    #     print(name)

f.close()
