#!/usr/bin/python3
# -*- coding:utf-8 -*-

import scrapy

'''
    First scrapy test
    url: 'http://books.toscrape.com'
'''

class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com']


    def parse(self, response):
        for book in response.xpath('//*[@id=\"default\"]/div/div/div/div/section/div[2]/ol/li/article[1]'):
            name = book.xpath('./h3/a/@title').extract_first()
            price = book.xpath('./div[@class=\"product_price\"]/p[@class=\"price_color\"]/text()').extract_first()
            # price = book.css('p.price_color: text').extract_first()
            yield {
                'name':name,
                'price':price,
            }

        next_url = response.xpath('//*[@id=\"default\"]/div/div/div/div/section/div[2]/div/ul/li[@class=\"next\"]/a/@href').extract_first()
        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)
