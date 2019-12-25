#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/12/16 16:39
# @Author : hushaobao
# @File   : study_Simulated_Login_selenium.py

from selenium import webdriver
from selenium.webdriver.common.by import By #用于指定 HTML 文件中 DOM 标签元素
from selenium.webdriver.support.ui import WebDriverWait #等待网页加载完成
from selenium.webdriver.support import expected_conditions as EC #指定等待网页加载结束条件


url = 'https://accounts.douban.com/passport/login'
# 实例化浏览器
broswer = webdriver.Chrome()
# 打开网页
broswer.get(url)
# 等待账户输入框元素出现
WebDriverWait(broswer,10).until(EC.presence_of_element_located((By.CLASS_NAME,'account-form')))
# 点击选择【密码登录】
pwd_login = broswer.find_element_by_xpath('//ul[@class="tab-start"]/li[2]').click()
# 定位账户，密码框
user = broswer.find_element_by_xpath('//input[@id="username"]')
pwd = broswer.find_element_by_xpath('//input[@id="password"]')
# 输入账户密码
user.click()
user.send_keys('你的账户')
pwd.click()
pwd.send_keys('你的密码')
# 找到登录按钮，点击【登录】
login = broswer.find_element_by_xpath('//a[@class="btn btn-account btn-active"]').click()


