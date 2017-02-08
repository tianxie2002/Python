
# coding=utf-8

import urllib2
import urllib

'''
菜谱详情的测试
'''
url = 'http://api.meishi.cc/v6/recipe_detail_new.php'

user_agent = 'model:phone;Version:meishij6.2.0;udid:8cbf44ed05053edfb795fe030a23008f5c3427fc;free:1;sInch:{750, 1334};sversion:10.2'
values = {
    'id':'1814205'
}

headers = {'User-Agent':user_agent}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()


print the_page
# 这个返回对象的字典对象，该字典描述了获取的页面情况。通常是服务器发送的特定头headers。目前是httplib.HTTPMessage 实例。
print response.info()
# 重定向的url
print response.geturl()


'''

'''