#!/usr/bin/env python
#encoding:UTF-8
import urllib
import urllib2
from bs4 import BeautifulSoup
import random,string
url ='http://www.dbmeinv.com/?pager_offset=1'
x=1
def loadImage(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    req =  urllib2.Request(url,headers=headers)#伪装浏览器访问
    page = urllib2.urlopen(req,timeout=20)#打开网页
    contents = page.read()#获取源码
    #html.parser解析网页xml功能更强大
    soup = BeautifulSoup(contents,'html.parser')#创建一个soup对象
    # 获取图片  find只找一次   find_all找到所有的标签    和正则表达式的区别
    my_girl = soup.find_all('img')
    for girl in my_girl:
        link = girl.get('src')
        #下载图片，取名字
        filename = string.join(random.sample(['a','b','c','d','e','f','g','h','i','j'], 4)).replace(" ","")
        print filename
        urllib.urlretrieve(link,'/home/python/Desktop/git_test/django2/image/%s.jpg'%filename)

while True:
    page = int(raw_input("输入下载第几页："))
    url = 'http://www.dbmeinv.com/?pager_offset=%s'%page
    loadImage(url)
print "下载完毕。。。。"
if __name__ == "__main__":
    loadImage(url)