import urllib.request
from lxml import etree
from bs4 import BeautifulSoup

type=[]
price=[]
info=[]

# 获取页码
# responseforpage = urllib.request.urlopen("https://search.jd.com/Search?keyword=%E4%B8%89%E6%98%9F%E6%89%8B%E6%9C%BA&enc=utf-8E&page=2",timeout=1)
# contentforpage = responseforpage.read().decode('utf-8')
# treeforpage=etree.HTML(contentforpage)
# pagenumber=treeforpage.xpath(u"//*[@id='J_bottomPage']/span[2]/em[1]/b/text()")
# print(pagenumber)

for i in range(0,52):
    url_i='https://search.jd.com/Search?keyword=%E4%B8%89%E6%98%9F%E6%89%8B%E6%9C%BA&enc=utf-8E&page='+str(i)
    # browser = webdriver.Chrome()
    # browser.get(url_i)
    # print(browser.page_source)
    # browser.close()
    response = urllib.request.urlopen(url_i,timeout=100)
    content = response.read().decode('utf-8')
    soup = BeautifulSoup(content, 'lxml')
    for link in soup.find_all(name='div',attrs={"class":"p-name p-name-type-2"}):
        # print(link)
        soup_link=BeautifulSoup(str(link), 'lxml')
        # print(soup_link.prettify())
        # print(soup_link.em)
        type.append(soup_link.em.text)
        # print(soup_link.em.text)
       # for k in em.find_all('em'):
       #     print(k)
       #     emmm = BeautifulSoup(str(k), 'lxml')
       #     print(emmm.string)
           # for i in em.find_all('font'):
           #     print(i)

    # for link in soup.find_all('em'):
    #     print(link)

    tree=etree.HTML(content)
    url_price=u"//*[@id='J_goodsList']/ul/li/div/div[3]/strong/i/text()"
#     url_type=u"////*[@id='J_goodsList']/ul/li/div/div[4]/a/em/text()[1]"
#     typelist=tree.xpath(url_type)
    pricelist= tree.xpath(url_price)
#     # print(typelist[0].attrib.get('title'))
    for i in pricelist:
        price.append(i)
#     for k in typelist:
#         type.append(k)
for i in range(0,1560):
    j=type[i]+' '+price[i]
    info.append(j)
print(info)
file=open('data.txt','w')
for line in info:
     file.write(line+'\n')
file.close()
# print(price)
# print(type)
