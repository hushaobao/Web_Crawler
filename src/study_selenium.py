#!/usr/bin/python

import requests
from time import sleep

from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_cookie():
    url = "https://weibo.com/5979786722/follow?rightmod=1&wvr=6"
    headers = {"User-agent": UserAgent().random, "Cookie": ""}
    response = requests.get(url, headers=headers)

    response.encoding = "utf-8"
    print(response.text)


def login_form():
    url = "https://accounts.douban.com/j/mobile/login/basic"
    headers = {
        "User-agent": UserAgent().random,
    }
    data = {"name": "zhanghao", "password": "mima"}
    response = requests.post(url, headers=headers, data=data)
    response.encoding = "utf-8"
    print(response.text)


def login_selenium():
    url = "https://accounts.douban.com/passport/login"

    broswer = webdriver.Chrome()
    broswer.get(url)

    WebDriverWait(broswer, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "account-form"))
    )

    pwd_login = broswer.find_element(By.XPATH, '//ul[@class="tab-start"]/li[2]').click()

    user = broswer.find_element(By.XPATH, '//input[@id="username"]')
    pwd = broswer.find_element(By.XPATH, '//input[@id="password"]')

    user.click()
    user.send_keys("你的账户")
    pwd.click()
    pwd.send_keys("你的密码")

    login = broswer.find_element(
        By.XPATH, '//a[@class="btn btn-account btn-active"]'
    ).click()


def web_driver():
    key = "爱情"
    url = "https://search.douban.com/book/subject_search?search_text={}&cat=1001&start=0".format(
        key
    )

    # 实例化浏览器对象
    broswer = webdriver.Chrome()

    # 打开网页
    broswer.get(url)

    while True:  # 循环翻页
        # 等待元素加载出来
        WebDriverWait(broswer, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "title-text"))
        )

        # 提取书名，评分，出版信息的标签
        book_names = broswer.find_elements(By.XPATH, '//a[@class="title-text"]')
        scores = broswer.find_elements(By.XPATH, '//span[@class="rating_nums"]')
        publish_infos = broswer.find_elements(By.XPATH, '//div[@class="meta abstract"]')

        # 从标签中提取数据
        for book_name, score, publish_info in zip(book_names, scores, publish_infos):
            book_name = book_name.text
            score = score.text
            publish_info = publish_info.text
            print((book_name, score, publish_info))

        # 定位 ‘后页’ 的元素，并点击
        next = broswer.find_elements(By.XPATH, '//a[@class="next false"]')
        sleep(5)  # 等待 1 秒，避免请求过快被封
        if next == []:  # 判断是否是最后一页
            break
        else:
            next[0].click()  # 定位'后页'的元素，并点击


if __name__ == "__main__":
    # web_driver()
    login_selenium()
