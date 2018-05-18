# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
def getContent(url):
    temp=""
    user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers={'User-Agent':user_agent}
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    content=response.read().decode('utf-8')
    pattern=re.compile('<div id="single-next-link" title=".*?>.*?<div class="content.*?>(.*?)</div>.*?</div>',re.S)
    items=re.findall(pattern,content)
    for x in items:
        temp+=x+"\n"
    return temp
def qiushibaike(a):
    result=""
    user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers={'User-Agent':user_agent}
    url="https://www.qiushibaike.com/text/page/"+str(a)+"/"
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    content=response.read().decode('utf-8')
    pattern=re.compile('<div class="article.*?>.*?<div class="author clearfix">.*?</div>'+
    '.*?<a href="(.*?)".*?class="contentHerf".*?>.*?<span>.*?</span>',re.S)
    items=re.findall(pattern,content)
    for x in items:
        result+=getContent('https://www.qiushibaike.com'+x)
    return result
r=qiushibaike(1)
print(r)