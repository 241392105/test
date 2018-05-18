#!/usr/bin/python
#-*- coding:utf-8 -*-
import urllib
import urllib2
import re
def Baidu(gjz):
    urls = 'http://www.baidu.com/s?wd='
    result=""
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    for i in range(5):
        url=urls+gjz+'&pn='+str(i*10)
        url=url.encode('utf-8')
        request = urllib2.Request(url,headers = headers)
        try:
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            pattern1 = re.compile('<h3 class="t.*?>.*?<a.*?href="(.*?)".*?>.*?</a>',re.S)
            address = re.findall(pattern1,content)
            pattern2 = re.compile('<h3 class="t.*?>.*?<a.*?>(.*?)</a>',re.S)
            display = re.findall(pattern2,content)
            for i in range(len(display)):
                result+=(display[i]+'\n'+address[i]+'\n')
        except:
            return result
    return result
def CTO(gjz):
    urls="http://so.51cto.com/index.php?keywords="
    result=""
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    for i in range(1,6):
        url=urls+gjz+'&p='+str(i)
        url=url.encode('utf-8')
        request=urllib2.Request(url,headers=headers)
        try:
            response=urllib2.urlopen(request)
            content=response.read().decode('utf-8')
            pattern=re.compile('<div class="res-doc.*?<h2.*?<a.*?href="(.*?)".*?>(.*?)</a>',re.S)
            items=re.findall(pattern,content)
            for i in items:
                result+=(i[1]+'\n'+i[0]+'\n')
        except:
            return result
    return result
def Taobao(gjz):
    urls='https://s.taobao.com/search?q='
    result=""
    user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers={'User-Agent':user_agent}
    s=[0,44,88,132,176]
    for i in s:
        url=urls+gjz+'&s='+str(i)
        url=url.encode('utf-8')
        request=urllib2.Request(url,headers=headers)
        try:
            response=urllib2.urlopen(request)
            content=response.read().decode('utf-8')
            pattern=re.compile('"nid":"(.*?)".*?"raw_title":"(.*?)",.*?"view_price":"(.*?)",',re.S)
            items=re.findall(pattern,content)
            for i in items:
                result+=(i[1]+"--"+i[2]+'元\n'+'https://item.taobao.com/item.htm?id='+i[0]+'\n')
        except:
            return result
    return result