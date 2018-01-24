#!/usr/bin/env python
#encoding:UTF-8
import urllib2
import urllib
import ssl
#忽略ssl安全认证
context = ssl._create_unverified_context()
url = "https://www.12306.cn/mormhweb/"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
request = urllib2.Request(url,headers=headers)
#添加到context参数里
response = urllib2.urlopen(request,context=context)
print response.read()