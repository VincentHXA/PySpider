#!/usr/bin/python3
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import urllib.request
from lxml import etree
from bs4 import BeautifulSoup
import time, threading
# from selenium import webdriver
infomation=[]
# 爬取5页信息
def webspider(i):
    # for i in range(1, number):
        url_i = 'https://search.jd.com/Search?keyword=%E4%B8%89%E6%98%9F%E6%89%8B%E6%9C%BA&enc=utf-8E&page=' + str(2 * i - 1)

        browser = webdriver.Chrome()
        browser.get(url_i)
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        # browser.execute_script('alert("To Bottom")')
        links = browser.find_elements(By.XPATH, "//*[@id=\"J_goodsList\"]/ul/li/div/div[1]/a")
        forward_links = [link.get_attribute("href") for link in links]
        browser.close()
        for link in forward_links:
            # print(link)
            response1 = urllib.request.urlopen(link)
            content1 = response1.read()
            soup1 = BeautifulSoup(content1, 'lxml')

            for link_soup in soup1.find_all(name='ul', attrs={"class": "parameter2 p-parameter-list"}):
                link_link = BeautifulSoup(str(link_soup), 'lxml')
                # print(len(link_link.find_all('li')))
                infomation1 = []
                for info in link_link.find_all('li'):
                    infomation1.append(info.text)
                infomation.append(infomation1)
t1 = threading.Thread(target=webspider, args=(1,))
t2 = threading.Thread(target=webspider, args=(2,))
t3 = threading.Thread(target=webspider, args=(3,))
t4 = threading.Thread(target=webspider, args=(4,))
t5= threading.Thread(target=webspider, args=(5,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

for inf in infomation:
    # print(inf)
    # file = open('data.txt', 'a')
    for i in inf:
        file = open('data.txt', 'a')
        file.write(i + '\n')
        file.close()
        # print(len(link))
#     soup = BeautifulSoup(str(link), 'lxml')
#     for link in soup.find_all(name='ul',attrs={"class":"parameter2 p-parameter-list"}):
#         print(link)



