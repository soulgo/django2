- 1、安装ubuntu 中PhantomJS的一个问题
```
sudo apt-get install nodejs
sudo apt-get install nodejs-legacy
sudo apt-get install npm
sudo npm -g install phantomjs-prebuilt
```
- 2、ubuntu python安装beautifulsoup4
```
pip install beautifulsoup4
```
- 3、安装scrapy
```
Python 2 / 3
安装非Python的依赖 sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
通过pip 安装 Scrapy 框架 sudo pip install scrapy
```
>scrapy.cfg ：项目的配置文件

>mySpider/ ：项目的Python模块，将会从这里引用代码

>mySpider/items.py ：项目的目标文件

>mySpider/pipelines.py ：项目的管道文件

>mySpider/settings.py ：项目的设置文件

>mySpider/spiders/ ：存储爬虫代码目录


