# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from scrapy.http import Request
from urllib import parse
from weibo.items import RunoobItem
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.selector import Selector

class RunoobSpider(scrapy.Spider):
    name = 'runoob'
    allowed_domains = ['www.runoob.com']
    start_urls = ['https://www.runoob.com/python/python-tutorial.html/']

    def start_requests(self):
        yield Request(url='https://www.runoob.com/python/python-tutorial.html', callback=self.parse)


    def parse(self, response):
        post_urls = response.xpath('//div[@class="design" and @id="leftcolumn"]/a/@href').extract()
        for post_url in post_urls:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)


    def parse_detail(self, response):
        runnoob_item = RunoobItem()
        title = response.xpath('//div[@id="content"]/h1').extract()
        content = response.xpath('//div[@id="content"]').extract()
        runnoob_item['title'] = title[0]
        runnoob_item['url'] = response.url
        runnoob_item['content'] = ""
        yield runnoob_item



