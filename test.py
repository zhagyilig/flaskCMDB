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
    print(l)