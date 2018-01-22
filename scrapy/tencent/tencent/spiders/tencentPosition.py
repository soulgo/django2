# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentpositionSpider(scrapy.Spider):
    name = "tencentPosition"
    allowed_domains = ["tencent.com"]
    url = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
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
            if self.offset < 1680:
                self.offset += 10
            else:
                break
            yield scrapy.Request(self.url + str(self.offset),callback=self.parse)

'''
//*[@id="position"]/div[1]/table//tr[2]/td[1]/a
#人数
//*[@id="position"]/div[1]/table/tbody/tr[2]/td[3]
#地点
//*[@id="position"]/div[1]/table/tbody/tr[3]/td[4]
#时间
//*[@id="position"]/div[1]/table/tbody/tr[2]/td[5]
'''