#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/11/25 18:34
# @Author : hushaobao
# @File   : study_ajax_1.py

# coding=gbk
from selenium import webdriver  # 打开浏览器
# 实现等待需要用到下面三个库
from selenium.webdriver.common.by import By  # 用于指定 HTML 文件中 DOM 标签元素
from selenium.webdriver.support.ui import WebDriverWait  # 等待网页加载完成
from selenium.webdriver.support import expected_conditions as EC  # 指定等待网页加载结束条件

key = '活着'
url = 'https://search.douban.com/book/subject_search?search_text={}&cat=1001&start=0'.format(key)

# 实例化浏览器对象
broswer = webdriver.Chrome()

# 打开网页
broswer.get(url)

while True:  # 循环翻页

    # 等待元素加载出来
    WebDriverWait(broswer, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'title-text')))

    # 提取书名，评分，出版信息的标签
    book_names = broswer.find_elements_by_xpath('//a[@class="title-text"]')
    scores = broswer.find_elements_by_xpath('//span[@class="rating_nums"]')
    publish_infos = broswer.find_elements_by_xpath('//div[@class="meta abstract"]')

    # 从标签中提取数据
    for book_name, score, publish_info in zip(book_names, scores, publish_infos):
        book_name = book_name.text
        score = score.text
        publish_info = publish_info.text
        print((book_name, score, publish_info))

    # 定位 ‘后页’ 的元素，并点击
    next = broswer.find_elements_by_xpath('//a[@class="next"]')
    if next == []:  # 判断是否是最后一页
        break
    else:
        next[0].click()   # 定位'后页'的元素，并点击
