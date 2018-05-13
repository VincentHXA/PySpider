# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

class ExamplesSpider(scrapy.Spider):
    name = 'examples'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index.html']

    def parse(self, response):
        # le = LinkExtractor(restrict_xpaths='//*[@id="matplotlib-examples"]/div/ul/li[@class="toctree-l1]/ul/li[@class="toctree-l2]', deny='/index.html$')
        le = LinkExtractor(restrict_xpaths='//*[@id="matplotlib-examples"]/div/ul/li/ul/li', deny='/index.html$')
        links = le.extract_links(response)
        print(len(links))
        for link in links:
            yield scrapy.Request(link.url, callback=self.parse_example)

    def parse_example(self,response):
        from ..items import MatplotlibExamplesItem
        href = response.xpath('//*[@id="animation-example-code-animate-decay-py"]/p[1]/a/@href').extract_first()
        url = response.urljoin(href)
        example = MatplotlibExamplesItem()
        example['file_urls'] = [url]
        return example
