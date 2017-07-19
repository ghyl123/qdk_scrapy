# qdk_scrapy

使用 scrapy 下载[青豆客图片](http://www.aisinei.com/forum-qingdouke-1.html)


## 安装
* python3
* scrapy

## 使用
先在根目录下建立一个名为img的文件夹.
如果你想自定义位置, 修改./tutorial/settings.py文件, 将其中的IMAGES_STORE修改为你想要的位置.

初始链接是 http://www.aisinei.com/forum-qingdouke-1.html

内容链接类似于 http://www.aisinei.com/thread-12853-1-1.html

写了三个spider:
* qdk : 下载一个内容链接
* qdklist : 从初始链接开始, 爬去所有的内容链接
* q : 整合前面两个, 下载所有内容链接

## 运行命令
cd 到根目录, 然后执行下面三个中的任意一个:

* scrapy crawl qdk -o qdk.jl
* scrapy crawl qdklist -o qdklist.jl
* scrapy crawl q -o q.jl

使用第一个命令的时候务必在 quotes_spider.py 中修改 start_urls 为你想要下载的内容链接.
或者这样运行命令

scrapy crawl qdk -o qdk.jl -a start_url="example.com"

example.com 修改为你想下载的内容链接.

## 日志
默认 LOG_LEVEL = 'ERROR' 
运行命令后无反应不要慌, 如果你想看到一连串输出, 修改为 INFO 即可.

## 错误
运行之后不能够保证一定能完整下载所有的图片, 尤其是运行scrapy crawl q -o q.jl.
遇到这种情况, 基本只能靠scrapy crawl qdk -o qdk.jl下载特定的内容链接.

## 微小的扩展性
理论上来说也适合这个[页面](http://www.aisinei.com/forum.php?gid=1)的板块.
青豆客只是其中之一. 简单试了下, 推女郎应该没问题.