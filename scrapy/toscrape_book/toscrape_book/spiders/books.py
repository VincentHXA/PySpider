# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from .items import BookItem

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        le_books = LinkExtractor(restrict_xpaths=u'//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article')
        for link in le_books.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_book)
        le_nextpage = LinkExtractor(restrict_xpaths=u'//*[@id="default"]/div/div/div/div/section/div[2]/div/ul/li[@class="next"]/a')
        links = le_nextpage.extract_links(response)
        if links:
            yield scrapy.Request(links[0].url, callback=self.parse)

    def parse_book(self, response):
        book = BookItem()
        sel = response.xpath(u'//*[@id="content_inner"]/article/div[1]/div[2]')
        book['name'] = sel.xpath(u'./h1/text()').extract_first()
        book['price'] = sel.xpath(u'./p[@class="price_color"]').xpath(u'./text()').extract_first()
        book['review_rating'] = sel.xpath('./p[contains(@class, "star-rating")]').re_first('star-rating ([A-Za-z]+)')
        # book['review_rating'] = sel.css('p.star-rating: attr(class)').re_first('star-rating ([A-Za-z]+)')
        sel = response.xpath(u'//*[@id="content_inner"]/article/table')
        book['upc'] = sel.xpath(u'(.//tr)[1]/td/text()').extract_first()
        book['stock'] = sel.xpath(u'(.//tr)[last()-1]/td/text()').re_first('\((\d+) available\)')
        book['review_num'] = sel.xpath(u'(.//tr)[last()]/td/text()').extract_first()
        yield book