# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

url='https://www.zhihu.com/explore'
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read()
    pattern=re.compile('<textarea.*?class="content">(.*?)</textarea.*?<div class="zh-summary summary clearfix">'+
    '(.*?)<a.*?</div>',re.S)
    items=re.findall(pattern,content)
    for item in items:
        print item[0]+"\n"
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason