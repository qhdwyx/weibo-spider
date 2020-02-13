# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
from urllib.parse import urlencode
from weibo.items import WeiboItem
from weibo.usersettings import headers, cookies, search_dict


class WeiboSpider(scrapy.Spider):
    name = 'weiboImg'
    allowed_domains = ['weibo.cn']
    start_urls = ['https://weibo.cn']
    search_url = 'https://s.weibo.com/weibo?'

    def start_requests(self):
        param = {
            "q" : "",
            "wvr" : "6",
            "b" : "1",
            "Refer" : "SWeibo_box"
        }
        for q in search_dict:
            param['q'] = q
            for i in range(search_dict[q]):
                if i > 0:
                    param['page'] = i + 1
                params = urlencode(param)
                url = self.search_url + params
                yield Request(url=url,headers=headers, cookies=cookies, callback=self.parse)

    def parse(self, response):
        catelog = parse.parse_qs(parse.urlparse(parse.unquote(response.url)).query)['q']
        item = WeiboItem()
        cardlist = response.xpath("//div[@class='card-feed']/div[@class='content']//li/img/@src").extract()
        item['catelog'] = catelog
        item['photos'] = cardlist
        yield item

