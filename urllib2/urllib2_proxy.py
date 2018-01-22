#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import django2.urllib2
import urllib
httpproxy_handler = django2.urllib2.ProxyHandler({"http": "61.135.217.7:80"})
nullproxy_handler = django2.urllib2.ProxyHandler({})

proxySwitch = True

if proxySwitch:
    opener = django2.urllib2.build_opener(httpproxy_handler)
else:
    opener = django2.urllib2.build_opener(nullproxy_handler)

request = django2.urllib2.Request("http://www.baidu.com/")
response = opener.open(request)
print response.read()