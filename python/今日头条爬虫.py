# -*- coding:utf-8 -*-

import urllib
import urllib2
import json

url="http://is.snssdk.com/api/news/feed/v51/?category=news_hot"
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User_Agent':user_agent}
request=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(request)
content=response.read()
rjson=json.loads(content)
rdata=rjson['data']
for i in rdata:
    rcontent=i['content']
    tcontent=json.loads(rcontent)
    print("title:"),
    print(tcontent['title'])
    print("keywords:"),
    try:
        print(tcontent['keywords'])
    except:
        print("no keywords")
    print("read count:"),
    print(tcontent['read_count'])
    print("share count:"),
    print(tcontent['share_count'])
    print("share url:"),
    print(tcontent['share_url'])
    print("------------------------------------------------------------------------")