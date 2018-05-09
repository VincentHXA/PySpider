#!/usr/bin/python3
# -*- coding: utf8 -*-

import urllib.request
import urllib.parse
import urllib.error
import socket

# urllib get
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# urllib post
# data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
# try:
#     response = urllib.request.urlopen('http://pythonsite.com/1111.html', data=data, timeout=1)
#     print(response.read())
#     print(type(response))
#     print(response.status)
#     print(response.getheaders())
# except urllib.error.HTTPError as e:
#     print(e.reason)
#     print(e.code)
#     print(e.headers)

# urllib request
# method 1
# url = 'http://httpbin.org/post'
# headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#            'Host': 'httpbin.org'}
# dict = {'name': 'vincent'}
# data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
# request = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
# response = urllib.request.urlopen(request)
# print(response.read())

