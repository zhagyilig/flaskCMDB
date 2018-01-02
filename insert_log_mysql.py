#!/usr/bin/env python3
# coding: utf-8
# Author: xtrdb.net
# File  : insert_log_mysql.py
# Time  : 2018/1/2

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
# cur.execute("select * from log")   # 测试连接库
# print(cur.fetchall())

res = {}
with open('nginx.log') as f:
    for line in f:
        if line == '\n':
            continue
        arr = line.split(' ')
        ip = arr[0]
        status = arr[8]
        res[(ip,status)] = res.get((ip, status),0) + 1

for l in sorted(res.items(),key=lambda x:x[1],reverse=True):
    cur.execute("insert into log(ip,status,count) values('%s','%s','%s')" %(l[0][0],l[0][1],l[1]))
