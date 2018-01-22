#!/usr/bin/env python
# -*- coding: utf-8 -*-
#	117.48.214.246	16816
#用户名：1406221797密码：lhisy32e
import django2.urllib2
import os
# 获取系统环境变量的授权代理的账户和密码
#Ubuntu的环境变量在.bashrc中设置
user = os.environ.get("proxyuser")
passwd = os.environ.get("proxypasswd")
#授权的代理账户密码拼接
authproxy_handler = django2.urllib2.ProxyHandler({"http": user + ":" + passwd + "@17.48.214.246:16816"})
# authproxy_handler = urllib2.ProxyHandler({"http":"1406221797:lhisy32e@17.48.214.246:16816"})
#构建一个自定义的handler
opener = django2.urllib2.build_opener(authproxy_handler)
#构建请求
request = django2.urllib2.Request("http://www.baidu.com/")
#获取相应
reponse = django2.urllib2.urlopen(request)
#打印类容
print reponse.read()