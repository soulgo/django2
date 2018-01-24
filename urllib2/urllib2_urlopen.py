#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import urllib2
# response = urllib2.urlopen("http://www.baidu.com")
# html = response.read()
# print html
ua_headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
}
wz = 'http://www.baidu.com'
request = urllib2.Request(wz,headers = ua_headers)
response = urllib2.urlopen(request)
html = response.read()
# print html
print response.getcode()
print response.geturl()
print response.info()