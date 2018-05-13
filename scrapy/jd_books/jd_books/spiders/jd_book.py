# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy_splash import SplashRequest

lua_script = '''
function main(splash)
splash: go(splash.args.url)
splash: wait(2)
splash: runjs("document.getElementsByClassName('page')[0].scrollIntoView(true)")
splash: wait(2)
return splash: html()
end
'''

class JdBookSpider(scrapy.Spider):
    name = 'jd_book'
    allowed_domains = ['search.jd.com']
    base_url = 'https://search.jd.com/Search?keyword=python&enc=utf-8&book=y&wq=python'

    def start_requests(self):
        yield Request(self.base_url, callback=self.parse_urls)

    def parse_urls(self, response):
        total = int(response.xpath('//*[@id="J_resCount"]/text()').extract_first().split("+")[0])
        pageNum = total // 60 + (1 if total % 60 else 0)
        for i in range(pageNum):
            url = '%s&page=%s' % (self.base_url, 2*i+1)
            yield SplashRequest(url, endpoint='execute', args={'lua_source':lua_script}, cache_args=['lua_source'])

    def parse(self, response):
        for sel in response.xpath('//*[@id="J_goodsList"]/ul/li[@class="gl-item"]'):
            yield {
                'name': sel.xpath('./div/div[@class="p-name"]').xpath('string(.//em)').extract_first(),
                'price': sel.xpath('./div/div[@class="p-price"]//i/text()').extract_first(),
            }
