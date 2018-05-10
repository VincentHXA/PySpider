import urllib.request
from lxml import etree
from bs4 import BeautifulSoup
# from selenium import webdriver
infomation=[]

for i in range(1,2):
    url_i='https://search.jd.com/Search?keyword=%E4%B8%89%E6%98%9F%E6%89%8B%E6%9C%BA&enc=utf-8E&page='+str(2*i-1)
# browser = webdriver.Chrome()
# browser.get("http://www.baidu.com")
# print(browser.page_source)
# browser.close()
    url=[]
    response = urllib.request.urlopen(url_i,timeout=100)
    content = response.read().decode('utf-8')
    soup = BeautifulSoup(content, 'lxml')
    for link in soup.find_all(name='div',attrs={"class":"p-name p-name-type-2"}):
        soup_link = BeautifulSoup(str(link), 'lxml')
        for k in soup_link.find_all('a'):
            url.append(k.get('href'))

         # link_children=BeautifulSoup(str(k), 'lxml')

for link in url:
    # print(link)
     link='https:'+link
     response1 = urllib.request.urlopen(link, timeout=100)
     content1 = response1.read()
     soup1 = BeautifulSoup(content1, 'lxml')

     for link_soup in soup1.find_all(name='ul', attrs={"class": "parameter2 p-parameter-list"}):
         link_link=BeautifulSoup(str(link_soup), 'lxml')
         # print(len(link_link.find_all('li')))
         infomation1=[]
         for info in link_link.find_all('li'):
             infomation1.append(info.text)
         infomation.append(infomation1)

# file=open('data.txt','w')
# for line in infomation:
#      file.write(line+'\n')
# file.close()
# print(len(infomation))
for inf in infomation:
    print(inf)
    # file = open('data.txt', 'a')
    for i in inf:
        file = open('data.txt', 'a')
        file.write(i+'\n')
        file.close()
    # file = open('data.txt', 'a')
    # for line in inf:
    #     file.write(line+'\n')
    #     file.close()



# print(url)