#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import django2.urllib2
import random
proxy_list = [
    {"180.110.167.196":"8118"},
    {"110.73.28.151":"8123"},
    {"113.221.13.27":"8888"},
    {"222.241.14.74":"8888"},
]

proxy = random.choice(proxy_list)
httpproxy_handler = django2.urllib2.ProxyHandler()
opener = django2.urllib2.build_opener(httpproxy_handler)
request = django2.urllib2.Request("http://www.baidu.com")
response = opener.open(request)
print response.read()