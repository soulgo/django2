# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YuehuiItem(scrapy.Item):
    #姓名
    name = scrapy.Field()
    #地址
    addres = scrapy.Field()
    #照片
    photo = scrapy.Field()
    #爱情观
    pcontent = scrapy.Field()