# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem

class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=']

    rules = (
        #问题首页的规则
        Rule(LinkExtractor(allow=r'page=\d+')),
        #点击问题进去之后的规则
        Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'),callback='parse_item'),
    )

    def parse_item(self, response):
        item = DongguanItem()
        item['title'] = response.xpath('//div[contains(@class, "pagecenter p3")]//strong/text()').extract()[0]
        item['number'] = item['title'].split(' ')[-1].split(':')[-1]
        content = response.xpath('//div[@class="contentext"]/text()').extract()
        if len(content) == 0:
            content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
            item['content'] = "".join(content).strip()
        else:
            item['content'] = "".join(content).strip()
        item['url'] = response.url
        yield item


