# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest

class LoginSpider(scrapy.Spider):
    name = 'Login'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/places/default/user/profile?_next=/places/default/edit/China-47']

    def parse(self, response):
        keys = response.xpath('//*[@id="web2py_user_form"]/form/table//label').xpath('./text()').re("(.+): ")
        values = response.xpath('//*[@id="web2py_user_form"]/form/table//td[@class="w2p_fw"]/text()').extract()
        yield dict(zip(keys, values))

    def start_requests(self):
        login_url = 'http://example.webscraping.com/places/default/user/login?_next=/places/default/edit/China-47'
        yield Request(login_url, callback=self.login)

    def login(self, response):
        sel = response.xpath('//*[@id="web2py_user_form"]/form/div/input')
        fd = dict(zip(sel.xpath('./@name').extract(), sel.xpath('./@value').extract()))
        fd['email'] = '136219065@qq.com'
        fd['password'] = '123456'
        request = FormRequest('http://example.webscraping.com/places/default/user/login?_next=/places/default/edit/China-47', formdata=fd, callback=self.parse_login)
        yield request

    def parse_login(self, response):
        if 'Welcome ' in response.text:
            yield from super().start_requests()



