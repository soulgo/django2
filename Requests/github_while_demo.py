#!/usr/bin/env python
# -*- coding: utf-8 -*-
#api https://api.github.com/repos/channelcat/sanic
#webapge https://www.github.com/channelcat/sanic
#当github主页发生变化之后，自动打开主页
'updated_at": "2018-03-04T13:55:31Z",'
import requests
import time
import webbrowser

api = 'https://api.github.com/repos/channelcat/sanic'
web_age = 'https://www.github.com/channelcat/sanic'
last_update = '2018-03-04T08:55:31Z'
all_info = requests.get(api).json()
cur_update = all_info['updated_at']
print cur_update

while True:
    if not last_update:
        last_update = cur_update
    if last_update < cur_update:
        webbrowser.open(web_age)
        print 'gothub主页发生变化了，赶紧去看吧'
    time.sleep(600)
