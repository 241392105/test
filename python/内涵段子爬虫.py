# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
 
url = 'http://neihanshequ.com/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode("utf-8")
    pattern = re.compile('<div class="content-wrapper".*?<h1 class="title".*?<p>(.*?)</p>.*?'+
    '<div class="options".*?data-text=.*?<span class="name">(.*?)</span>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print(item[1]+"\n"+item[0]+"\n\n")
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason