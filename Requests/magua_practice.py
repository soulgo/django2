#!/usr/bin/env python
# -*- coding: utf-8 -*-
#在某个路径下查询特定文件
import os
path = '/home/python/Desktop/git_test/django2/scrapy/yuehui'
files = os.listdir(path)
for f in files:
    if 'douban' in f and f.endswith('.png'):
        print 'Found it' + f