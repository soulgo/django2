 # -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json

class TencentPipeline(object):
    def __init__(self):
        self.fileNmae = codecs.open("dongguan.json","w",encoding="utf-8")
        # self.fileNmae = open("dongguan.json","w")
    def process_item(self, item, spider):
        context = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.fileNmae.write(context)
        return item
    def close_spider(self,spider):
        self.fileNmae.close()


'''
//*[@id="morelist"]/div/table[2]/tbody/tr/td/table/tbody/tr[3]/td[2]/a[2]
'''