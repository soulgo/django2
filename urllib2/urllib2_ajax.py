#!/usr/bin/env python
#encoding:UTF-8
import django2.urllib2
import urllib
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
# start = raw_input("请输入起始数字：")
# limit = raw_input("请输入终止数字：")
formdata = {
    # "start":start,
    # "limit":limit
    "start":"0",
    "limit":"20"
}
data = urllib.urlencode(formdata)
request = django2.urllib2.Request(url, headers=headers, data=data)
response = django2.urllib2.urlopen(request)
print response.read()
