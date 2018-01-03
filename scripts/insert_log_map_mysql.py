#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author : xtrdb.net
# File   : insert_log_map_mysql.py
# Time   : 2018/1/3


import MySQLdb as mysql
import requests

# 连接数据库配置
conn= mysql.connect(
        host='localhost',
        port = 9036,
        user='root',
        passwd='888888',
        db ='reboot12',
        unix_socket = '/tmp/mysql9036.sock',
        )
cur = conn.cursor()
conn.autocommit(True)

res = {}
with open('/tmp/test_access.log') as f:
    for line in f:
        if line == '\n':
            continue
        arr = line.split(' ')
        ip = arr[0]   # 来源ip
        status = arr[8]  # http状态码
        res[(ip,status)] = res.get((ip, status),0) + 1  # ip 状态码聚合


def getXY(ip):
    # 通过ip调用百度地图api获取原来地址
    url = 'http://api.map.baidu.com/location/ip?ak=fAWnTdrFaHUE1L2n6QBAusbrjcESPruF&coor=bd09ll&ip='
    r = requests.get(url + ip)
    return r.json()

for (ip,status),count in res.items():
    # 插入相应信息到MySQL
    res = getXY(ip)
    if res['status'] == 0:
        x = res['content']['point']['x']
        y = res['content']['point']['y']
        sql = "insert into log_map(ip,x,y,status,count) values('%s','%s','%s','%s','%s')" %(ip,x,y,status,count)
        print(sql) # 输出sql
        cur.execute(sql)

print('success')


