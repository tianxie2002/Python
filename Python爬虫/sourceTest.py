#coding=utf-8

import re


f = open("source","r")
res = ""
while True:
    line = f.readline()
    if line:
        res +=  line + "\n"
    else:
        break
# print res


myItems = re.findall('<div.*?class="content".*?>(.*?)</div>', res, re.S)
for s in myItems:
    if s:
        print s.replace("\n","").replace("<span>","").replace("</span>","").replace("<br>","\n")
        print "---------------"

print "+++++++++++++++++++++"

myItems = re.findall('<img.*?src="(.*?)"', res, re.S)
images = []
for s in myItems:
    if s and s.startswith("http"):
        print s
        images.append(s)
        # print s.replace("\n","").replace("<span>","").replace("</span>","").replace("<br>","\n")
        print "---------------"


