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

## 日志
默认 LOG_LEVEL = 'ERROR' 
运行命令后无反应不要慌, 如果你想看到一连串输出, 修改为 INFO 即可.

