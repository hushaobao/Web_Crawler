#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/12/18 21:49
# @Author : hushaobao
# @File   : study_multiprocessing_1.py


from multiprocessing import Pool
import os
import time
import random


"""
Pool 可以提供指定数量的进程供用户调用，默认大小是 CPU 的核数。但有新的请求提交到
Pool 中时，池还没有满，就会创建一个新的进程用来执行该请求；如已达到最大数，就会等待
知道有进程结束，才会创建新的进程来处理他
"""


def run_task(name):
    print('Task %s (pid = %s) is running ...' % (name, os.getpid()))
    time.sleep(random.random() * 3)
    print('Task %s end.' % name)


if __name__ == '__main__':
    print('Current process %s.' % os.getpid())  # os.getpid() 获得进程 id
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))   # 添加进程任务，i 为传进去的进程任务的参数
        pass
    print('Waiting for all subprocesses done...')
    p.close()  # 不再添加新进程
    p.join()  # 等待所有子进程执行完毕,调用之前必须先调用close(),针对 Pool 对象
    print('All subprocesses done.')