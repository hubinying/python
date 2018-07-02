# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 13:55:56 2018

@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
la=re.compile('"description":"(.*?)"').findall(data)
la1=re.compile('"temp":(.*?)"').findall(data)
la2=re.compile('"pressure":(.*?)"').findall(data)
for i in range(37):
    print('天气情况：{}\t,温度：{}\t,气压：{}\t'.format(la[i],la1[i],la2[i]))









