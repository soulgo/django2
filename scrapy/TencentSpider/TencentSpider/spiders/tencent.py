# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
# 导入链接规则匹配类，用来提取符合规则的连接
from scrapy.spiders import CrawlSpider, Rule
from TencentSpider.items import TencentItem

class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0']
    # Response里链接的提取规则，返回的符合匹配规则的链接匹配对象的列表
    pagelink = LinkExtractor(allow=("start=\d+"))

    rules = [
        # 获取这个列表里的链接，依次发送请求，并且继续跟进，调用指定回调函数处理
        Rule(pagelink,callback="parse_item",follow=True)
    ]

    def parse_item(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentItem()
            # 职位姓名
            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 职位链接
            item['positionlink'] = "https://hr.tencent.com/" +each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['positionNum'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]
            yield item
