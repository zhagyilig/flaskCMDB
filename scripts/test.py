#!/usr/bin/env python3
# coding: utf-8
# Author: xtrdb.net
# File  : test.py
# Time  : 2017/12/31

# import requests
# from pyquery import PyQuery as pq
#
#
# url = 'https://movie.douban.com/top250'
# res = requests.get(url)
#
# # print(res.text)
#
# d = pq(res.text)
# # print(d('.title').html())
# for title in d('.title'):
#     print(pq(title).html())


# res = {}
#
# with open('nginx.log') as f:
#     for line in f:
#         if line == '\n':
#             continue
#         arr = line.split(' ')
#         ip = arr[0]
#         status = arr[8]
#         res[(ip,status)] = res.get((ip, status),0) + 1
#
# for l in sorted(res.items(),key=lambda x:x[1],reverse=True):
#     print(l)

import requests

def getXY(ip):
    '''获取ip地址的经纬度函数'''
    url = 'http://api.map.baidu.com/location/ip?ak=fAWnTdrFaHUE1L2n6QBAusbrjcESPruF&coor=bd09ll&ip='
    r = requests.get(url+ip)
    print(r.json()['content']['point'])

try:
    getXY('192.168.9.74')
except KeyError as e:
    print('%s key not exist.'%e)
