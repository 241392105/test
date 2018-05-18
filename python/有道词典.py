# -*- coding:utf-8 -*-

import urllib
import urllib2
import json

words=raw_input()
url="http://dict.youdao.com/suggest?q="+words+"&le=eng&doctype=json"
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User_Agent':user_agent}
request=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(request)
content=response.read().decode('utf-8')
jcontent=json.loads(content)
jdata=jcontent['data']
jentries=jdata['entries']
for i in jentries:
    print(i['entry'])
    print(i['explain'])
    print("------------------------------------------------------")