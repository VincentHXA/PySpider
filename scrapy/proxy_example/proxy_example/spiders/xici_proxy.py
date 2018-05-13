# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json

class XiciProxySpider(scrapy.Spider):
    name = 'xici_proxy'
    allowed_domains = ['www.xicidaili.com']

    def start_requests(self):
        for i in range(1,4):
            yield Request('http://www.xicidaili.com/nn/%s' % i)

    def parse(self, response):
        for sel in response.xpath('//table[@id="ip_list"]/tr[position()>1]'):
            ip = sel.xpath('./td[2]/text()').extract_first()
            port = sel.xpath('./td[3]/text()').extract_first()
            schema = sel.xpath('./td[6]/text()').extract_first().lower()

            url = '%s://httpbin.org/ip' % schema
            proxy = '%s://%s:%s' % (schema,ip,port)
            meta = {
                'proxy':proxy,
                'dont_retry':True,
                'download_timeout':10,
                '_proxy_schema': schema,
                '_proxy_ip': ip,
            }
            yield Request(url, callback=self.check_available, meta=meta, dont_filter=True)

    def check_available(self, response):
        proxy_ip = response.meta['_proxy_ip']
        if proxy_ip == json.loads(response.text)['origin']:
            yield {
                'proxy_schema': response.meta['_proxy_schema'],
                'proxy': response.meta['proxy'],
            }

class TestRandomProxySpider(scrapy.Spider):
    name = 'test_random_proxy'
    def start_requests(self):
        for i in range(100):
            yield Request('http://httpbin.org/ip', dont_filter=True)
            yield Request('https://httpbin.org/ip', dont_filter=True)

    def parse(self, response):
        print(json.loads(response.text))