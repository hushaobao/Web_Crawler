# 获取成时GDP人口


import re
import csv
from time import sleep
from tqdm import tqdm
from lxml import etree
from utils import get_url
from bs4 import BeautifulSoup


def get_GDP_infos():
    url = "http://caifuhao.eastmoney.com/news/20190201115604564011000"
    html = get_url(url)
    # pat = '<p>(\d+.*?)</p>|<p><strong>(\d+.*?)</p>'
    # infos = re.findall(pat, html, re.S)
    infos = re.findall("<br><p>(\d+.*?)</p>", html, re.S)

    data = []
    for info in infos:
        pat1 = r"(\d+?)亿元"
        GDP = re.findall(pat1, info)
        pat2 = r"人口：(\d.*)）"
        people_num = re.findall(pat2, info)
        pat3 = r"\.(.*?)\d+?亿元"
        city = re.findall(pat3, info)

        frame = {"city ": city, "people_num ": people_num, "GDP ": GDP}
        print(frame)
        data.append(frame)
    return data


def get_douban_book_infos():
    urls = [
        "https://book.douban.com/top250?start={}".format(str(i * 25))
        for i in range(0, 250 // 25)
    ]
    infos = []
    for url in urls:
        HTML = get_url(url)
        html = etree.HTML(HTML)
        ls = html.xpath('//tr[@class="item"]')

        for info in ls:
            ch_name = (
                info.xpath("./td[2]/div[1]/a/text()")[0]
                .replace("\n", "")
                .replace(" ", "")
            )
            try:
                en_name = info.xpath("./td[2]/div[1]/span/text()")[0]
            except Exception as e:
                print(e)
                en_name = "None"
            pub_info = info.xpath("./td[2]/p[1]/text()")[0]
            score = info.xpath("./td[2]/div[2]/span[2]/text()")[0]
            score_num = (
                info.xpath("./td[2]/div[2]/span[3]/text()")[0]
                .replace("\n", "")
                .replace(" ", "")
            )

            info = {
                "name": ch_name,
                "en_name": en_name,
                "出版信息": pub_info,
                "评分": score,
                "评分人数": score_num,
            }
            infos.append(info)
            print(info)
    return infos


def get_macdonalds_infos():
    def parser_html(html):
        pat1 = "<span>城市</span>(.*?)</td>"
        cities = [i.replace(" ", "") for i in re.findall(pat1, html, re.S)]

        pat2 = "<span>门店编号</span>(.*?)</td>"
        number = [i.replace(" ", "") for i in re.findall(pat2, html, re.S)]

        pat3 = "<span>门店名称</span>(.*?)</td>"
        shop_names = [i.replace(" ", "") for i in re.findall(pat3, html, re.S)]
        info = zip(cities, number, shop_names)
        return info

    urls = [
        "https://www.mcdonalds.com.cn/index/Quality/publicinfo/deliveryinfo?_ga=0&page={}".format(
            str(i)
        )
        for i in range(1, 243)
    ]
    save_path = "data/mcdonalds_infos.csv"
    with open(save_path, "w", encoding="utf-8-sig", newline="") as f:
        # 创建写入对象
        writer = csv.writer(f)
        # 写入第一行头信息
        writer.writerow(["city", "number", "shop_name"])

        for url in tqdm(urls):
            sleep(0.1)
            html = get_url(url)
            if html is None:
                print(f"{url} 请求失败...")
                continue
            infos = parser_html(html)
            for inf in infos:
                writer.writerow(inf)


def get_kugou_music_top500_infos():
    urls = [
        f"https://www.kugou.com/yy/rank/home/{i}-23784.html?from=rank"
        for i in range(1, 24)
    ]

    infos = []
    for url in urls:
        HTML = get_url(url)
        sleep(0.05)
        html = BeautifulSoup(HTML, "lxml")
        # html.cssselect('.xz_det.fr > p.txt')[0].text
        # ranks = html.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num')  # noqa
        # names = html.select('#rankWrap > div.pc_temp_songlist > ul > li > a')  # noqa
        # times = html.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')  # noqa
        ranks = html.find_all("span", class_="pc_temp_num")
        names = html.find_all("a", class_="pc_temp_songname")
        times = html.find_all("span", class_="pc_temp_time")

        for r, n, t in zip(ranks, names, times):
            # embed()
            r = r.get_text().replace("\n", "").replace("\t", "").replace("\r", "")
            n = n.get_text()
            n = re.sub(r"\s+", "", n)
            t = t.get_text().replace("\n", "").replace("\t", "").replace("\r", "")
            data = {"排名": r, "歌名-歌手": n, "播放时间": t}
            infos.append(data)
            print(data)
    return infos


if __name__ == "__main__":
    # get_GDP_infos()
    # get_douban_book_infos()
    # get_macdonalds_infos()
    get_kugou_music_top500_infos()
