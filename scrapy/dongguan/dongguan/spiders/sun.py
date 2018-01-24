# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem

class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    # start_urls = ['http://wz.sun0769.com/index.php/question/report?page=']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    # rules = (
    #     Rule(LinkExtractor(allow=r'report\?page=\d+'), callback='parse_item', follow=True)
    # )
    rules = (
        Rule(LinkExtractor(allow=r'type=4\&page=\d+')),
        Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'),callback='parse_item'),
    )

    def parse_item(self, response):
        item = DongguanItem()
        # item['title'] = response.xpath('//div[contains(@class,"pagecenter p3")]//strong/text()').extract()[0]
        item['title'] = response.xpath('//div[contains(@class, "pagecenter p3")]//strong/text()').extract()[0]
        item['number'] = item['title'].split(' ')[-1].split(':')[-1]
        item['content'] = response.xpath('//div[@class="c1 text14_2"]/text()').extract()[0]
        item['url'] = response.url
        yield item





'''
//div[contains(@class,'pagecenter p3')]//strong/text()
//*[@id="morelist"]/div/table[2]/tbody/tr/td/table/tbody/tr[1]/td[2]/a[2]
/html/body/div[6]/div/div[1]/div[1]/strong
'''