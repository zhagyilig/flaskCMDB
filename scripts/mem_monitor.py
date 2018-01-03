#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author : xtrdb.net
# File   : mem_monitor.py
# Time   : 2018/1/3


import psutil
import time
import MySQLdb as mysql

conn= mysql.connect(    # 连接MySQL
        host='localhost',
        port = 9036,
        user='root',
        passwd='888888',
        db ='reboot12',
        unix_socket = '/tmp/mysql9036.sock',
        )

cur = conn.cursor()
conn.autocommit(True)

def monit_mem():
    while True:
        memfree = psutil.virtual_memory().free/1024/1024
        sql = 'insert into mem(mem,time) values("%s","%s")' %(memfree,time.time())
        cur.execute(sql)
        time.sleep(1)

monit_mem()

