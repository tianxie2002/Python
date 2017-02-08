#!/usr/bin/python

# coding=utf-8

import urllib2

# '''
# 一般的抓取页面代码 1
# '''
# response = urllib2.urlopen("http://www.baidu.com")
#
# html = response.read()
#
# print  html

# '''
# 一般的抓取页面代码2
# '''
# req = urllib2.Request("http://www.baidu.com")
#
# response = urllib2.urlopen(req)
#
# the_page = response.read()
#
# print the_page


# '''
# 带参数 表单提交 POST
# '''
# import  urllib
#
# url = 'http://www.baidu.com'
# values = {
#     'name':'LP',
#     'location':'BJ',
#     'language':'Python'
# }
#
# #编码
# data = urllib.urlencode(values)
#
# req = urllib2.Request(url,data)
#
# response = urllib2.urlopen(req)
#
# the_page = response.read()
# print the_page


# '''
# get方式传送参数
# '''
# import urllib
#
# data = {}
# data['name'] = "PL"
# data['location'] = 'Location'
# data['language'] = 'Python'
#
# url_values = urllib.urlencode(data)
#
# url = "http://www.baidu.com"
# full_url = url+'?' + url_values
# data = urllib2.urlopen(full_url)
# print data.read()

'''
设置header到http请求中
'''
import urllib

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
