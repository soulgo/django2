# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yuehui.items import YuehuiItem

class WangyiSpider(CrawlSpider):
    name = 'wy'
    allowed_domains = ['yuehui.163.com']
    start_urls = ['http://yuehui.163.com/searchusers.do?sex=0&ageBegin=18&ageEnd=25&province=0&city=0#userlist-top']
    page_links = LinkExtractor(allow=(r"yuehui.163.com/searchusers.do?sex=0&ageBegin=18&ageEnd=25&province=0&city=0#userlist-top"))
    profile_links = LinkExtractor(allow=(r"yuehui.163.com/viewuser.do?id=\d+"))
    rules = (
        Rule(page_links),
        Rule(profile_links,callback="parse_item",follow=True)
    )

    def parse_item(self, response):
       item = YuehuiItem()
       # 姓名
       item['name'] = self.get_name(response)
       # 地址
       item['addres'] = self.get_addres(response)
       # 照片
       item['photo'] = self.get_photo(response)
       # 爱情观
       item['pcontent'] = self.get_pcontent(response)
       yield item

    def get_name(self,response):
        name = response.xpath('//div[@class="pcontent"]//div[@class="nickwrap"]/p/text()').extract()
        print name
        if len(name):
            name = name[0]
        else:
            name = "NULL"
        return name.strip()

    def get_addres(self,response):
        addres = response.xpath('//div[@class="pcontent"]//div[@class="biwrap"]/ul/li/p[@class="left"]/span[2]').extract()
        if len(addres):
            addres = addres[0]
        else:
            addres = "NULL"
        return addres.strip()

    def get_photo(self,response):
        photo = response.xpath('//div[@class="pcontent"]/div[@class="prwrap"]//img/@src').extract()
        if len(photo):
            photo = photo[0]
        else:
            photo = "NULL"
        return photo.strip()

    def get_pcontent(self,response):
        pcontent = response.xpath('//div[@class="pcontent pcontent-visitor"]/ul[2]').extract()
        if len(pcontent):
            pcontent = pcontent[0]
        else:
            pcontent = "NULL"
        return pcontent.strip()