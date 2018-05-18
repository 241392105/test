# -*- coding:utf-8 -*-

import urllib
import urllib2
import json

townID="CHLN130000"
url="http://tj.nineton.cn/Heart/index/all?city="+townID
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User_Agent':user_agent}
request=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(request)
content=response.read()
jcontent=json.loads(content)
jweather=jcontent['weather']
for i in jweather:
    jtoday=i['today']
    jsuggestion=jtoday['suggestion']
    jflu=jsuggestion['flu']
    print(jflu['brief'])