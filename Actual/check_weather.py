#!/usr/bin/env python
#encoding:UTF-8
import requests
from collections import Iterable,Iterator
'''
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5
出现编码问题时，加入下面三行代码
Python的str默认是ascii编码，和unicode编码冲突
'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0

    def getWeather(self,city):
        r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s:%s,%s,%s' % (city,data['low'],data['high'],data['date'])
    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)
#u'北京',u'天水',u'西安',u'广州'
if __name__ == "__main__":
        print "输入exit退出查询"
        while True:
            city = raw_input("请输入需要查询天气的城市:")
            if city == 'exit':
                quit()
            else:
                for x in WeatherIterable([city]):
                    print x