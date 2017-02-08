#coding=utf-8

import urllib2
import urllib
import re
import thread
import time

class Spider_model:
    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False

    def GetPage(self,page):
        myUrl = "http://www.qiushibaike.com/imgrank/" + str(page)
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {'User-Agent': user_agent}

        req = urllib2.Request(myUrl, headers=headers)
        myResponse = urllib2.urlopen(req)
        myPage = myResponse.read()
        unicodePage = myPage.decode('utf-8')
        # print unicodePage

        myItems = re.findall('<div.*?class="content">(.*?)</div>', unicodePage, re.S)

        items = []
        for item in myItems:
            con = item.replace("<br/>","\n").replace("\n","").replace("<span>","").replace("</span>","")
            print "---------------"
            print con
            items.append(con)
        return items


    def LoadPage(self):
        while self.enable:
            if len(self.pages) < 2:
                try:
                    myPage = self.GetPage(str(self.page))
                    self.page += 1
                    self.pages.append(myPage)
                except:
                    print "无法连接糗事百科"
            else:
                time.sleep(1)

    def ShowPage(self,nowPage,page):
        for items in nowPage:
            print "第%d页"%page,items[0],items[1]
            myInput = raw_input()
            if myInput == "quit":
                self.enable = False
                break
    def Start(self):
        self.enable = True
        page = self.page
        print  "正在加载中......"

        thread.start_new_thread(self.LoadPage())

        while self.enable:
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage,page)
                page += 1


# ----------- 程序的入口处 -----------
print u"""
---------------------------------------
   程序：糗百爬虫
   版本：0.3
   作者：why
   日期：2014-06-03
   语言：Python 2.7
   操作：输入quit退出阅读糗事百科
   功能：按下回车依次浏览今日的糗百热点
---------------------------------------
"""

print u'请按下回车浏览今日的糗百内容：'
raw_input(' ')
myModel = Spider_model()
myModel.Start()
# myModel.GetPage(1)

