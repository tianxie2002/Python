# coding=utf-8

import re

pattern = re.compile(r"hello")

m1 = pattern.match("hello world")
m2 = pattern.match("helloo world")
m3 = pattern.match("helllo world")

if m1:
    print m1.group()
else:
    print "m1无法匹配"


if m2:
    print m2.group()
else:
    print "m2无法匹配"


if m3:
    print m3.group()
else:
    print "m3无法匹配"


newpattern = re.compile(r"\d+\.\d*")
m1 = newpattern.match("3.1415")
m2 = newpattern.match("33")

if m1:
    print m1.group()
else:
    print "m1不是小数"

if m2:
    print m2.group()
else:
    print "m2不是小数"


m = re.match(r'hello', 'hello world! 1world')
print m.group()


p = re.compile(r'world')
m = re.search(p,"hello world")
if m:
    print m.group()

