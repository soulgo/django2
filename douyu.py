#!/usr/bin/env python
#encoding:UTF-8
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup
class douyuSelenium(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        self.driver = webdriver.PhantomJS()

    #具体的测试用例方法，一定要以test开头
    def testDouyu(self):
        self.driver.get('http://www.douyu.com/directory/all')
        while True:
            # 指定xml解析
            soup = BeautifulSoup(self.driver.page_source, 'xml')
            # 返回当前页面所有房间标题列表 和 观众人数列表,UP主，播放类型
            titles = soup.find_all('h3', {'class': 'ellipsis'})
            nums = soup.find_all('span', {'class': 'dy-num fr'})
            peoples = soup.find_all('span',{'class':'dy-name ellipsis fl'})
            tags = soup.find_all('span', {'class': 'tag ellipsis'})


            # 使用zip()函数来可以把列表合并，并创建一个元组对的列表[(1,2), (3,4)]
            for title,num,people,tag in zip(titles,nums,peoples,tags):
                print u"房间标题:" + title.get_text().strip(), \
                    u"\t观众人数: " + num.get_text().strip(), \
                    u"\t作者: " + people.get_text().strip(), \
                    u"\t播放类型: " + tag.get_text().strip()
            # page_source.find()未找到内容则返回-1
            if self.driver.page_source.find('shark-pager-disable-next') != -1:
                break
            # 模拟下一页点击
            self.driver.find_element_by_class_name('shark-pager-next').click()

    # 退出时的清理方法
    def tearDown(self):
        print '加载完成...'
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()