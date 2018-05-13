#!/usr/bin/python3
# -*- coding: utf-8 -*-

import scrapy

class BookItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    review_rating = scrapy.Field()  # review rating : from 1 to 5
    review_num = scrapy.Field() # review number
    upc = scrapy.Field() # book unique code
    stock = scrapy.Field()
