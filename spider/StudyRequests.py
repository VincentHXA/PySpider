#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests

# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
# }
# data = {"name":"vincent"}
#
# response = requests.post("https://www.zhihu.com", headers=headers, data=data)
# print(response.text)

# upload file
# files = {"files":open("Text.txt","rb")}
# response = requests.post("http://httpbin.org/post",files=files)
# print(response.text)

# get cookies
# response = requests.get("http://www.baidu.com")
# for key,value in response.cookies.items():
#     print(key,"=",value)

# session
# session = requests.Session()
# session.get("http://httpbin.org/cookies/set/number/123456")
# response = session.get("http://httpbin.org/cookies")
# print(response.text)

# certificate
response = requests.get("https:/www.12306.cn")
print(response.status_code)