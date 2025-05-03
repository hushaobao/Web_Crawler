# 网易云音乐API接口

> reference： https://mp.weixin.qq.com/s/ZxqRmTVKTcunMw023m5wug

## 1、网易云音乐评论 api 接口

```bash
# offset: 偏移量(翻页), offset需要是limit的倍数
# limit: 返回数据条数(每页获取的数量), 默认为20, 可以自行更改

http://music.163.com/api/v1/resource/comments/R_SO_4_{musicID}?limit=20&offset=0

```

## 2、个人信息api 接口

```bash
# userID: 用户 id
https://music.163.com/api/v1/user/detail/{userID}
```

## 3、歌词api接口

```bash
https://music.163.com/api/song/lyric?id={musicID}&lv=1&kv=1&tv=-1
```

## 4、歌单api

```bash
# id=19723756, 云音乐飙升榜
# id=3779629, 云音乐新歌榜
# id=3778678, 云音乐热歌榜
# id=2250011882, 抖音排行榜
https://music.163.com/api/playlist/detail?id={歌单ID}
```

## 5、搜索

```bash

# 参数:
#     limit: 返回数据条数(每页获取的数量）, 默认为20, 可以自行更改
#     offset: 偏移量(翻页）, offset需要是limit的倍数
#     type: 搜索的类型
#         type=1           单曲
#         type=10          专辑
#         type=100         歌手
#         type=1000        歌单
#         type=1002        用户
#         type=1004        MV
#         type=1006        歌词
#         type=1009        主播电台

http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={搜索内容}&type=1&offset=0&total=true&limit=20

```


## 6、其他

```bash
# 歌手专辑
http://music.163.com/api/artist/albums/{歌手ID}?id={歌手ID}&offset=0&total=true&limit=10

# 专辑信息
http://music.163.com/api/album/{专辑ID}?ext=true&id={专辑ID}&offset=0&total=true&limit=10

# 歌曲信息
http://music.163.com/api/song/detail/?id={歌曲ID}&ids=%5B{歌曲ID}%5D

# MV
http://music.163.com/api/mv/detail?id={MV的ID}&type=mp4
```