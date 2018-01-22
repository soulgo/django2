#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import django2.urllib2
import json
from lxml import etree
url = "https://www.qiushibaike.com/8hr/page/2/"
headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
request = django2.urllib2.Request(url, headers=headers)
html = django2.urllib2.urlopen(request).read()
text = etree.HTML(html)

node_list = text.xpath('//div[contains(@id, "qiushi_tag")]')
items = {}
for node in node_list:
    # xpath返回的列表，这个列表就这一个参数，用索引方式取出来，用户名
    # username = node.xpath('./div/a/@title')[0]
    # 图片连接
    # image = node.xpath('.//div[@class="thumb"]//@src')#[0]
    # 取出标签下的内容,段子内容
    content = node.xpath('.//div[@class="content"]/span')[0].text
    # 取出标签里包含的内容，点赞
    # zan = node.xpath('.//i')[0].text
    # 评论
    # comments = node.xpath('.//i')[1].text

    items = {
        # "username" : username,
        # "image" : image,
        "content" : content,
        # "zan" : zan,
        # "comments" : comments
    }
    with open("qushi.json","a") as f:
        f.write(json.dumps(items,ensure_ascii=False).encode("utf-8") + "\n")