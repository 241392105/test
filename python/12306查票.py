# -*- coding:utf-8 -*-

import urllib
import urllib2
import json

url="https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-12-22&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=0X00"
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User_Agent':user_agent}
request=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(request)
content=response.read().decode('utf-8')
jcontent=json.loads(content)
jdata=jcontent['data']
jresult=jdata['result']
list=[]
for i in jresult:
    list.append(i)
for i in list:
    t=i.split('|')
    print(t[1]),
    print(t[2]),
    print(t[3]),
    print(t[4]),
    print(t[5]),
    print(t[8]),
    print(t[9]),
    print(t[10]),
    print(t[13]),
    print(t[30]),
    print(t[31]),
    print(t[32])
    print("----------------------------------------------------------------------")