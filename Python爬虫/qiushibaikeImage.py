#coding=utf-8

import re
import urllib2

# http://www.qiushibaike.com/imgrank/

def GetData(page):
    'http://tieba.baidu.com/p/4967568493?pn='

    # myUrl = "http://www.qiushibaike.com/imgrank/" + str(page)
    myUrl = "http://tieba.baidu.com/p/4967568493?pn=" + str(page)
    user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    headers = {'User-Agent': user_agent}

    req = urllib2.Request(myUrl, headers=headers)
    myResponse = urllib2.urlopen(req)
    if myResponse:
        myPage = myResponse.read()
        unicodePage = myPage.decode('utf-8')
        # print unicodePage

        myItems = re.findall('<img.*?src="(.*?)"', unicodePage, re.S)
        for it in myItems:
            if it and it.startswith("http") and not it.startswith("http://static.tieba.baidu.com/tb"):
                print it


for i in range(1,10):
    print i
    GetData(i)
