# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:48:22 2018
全球未来5天气预报
2018-06-21 03:00:00    按照3小时一次预报
2018-06-21 06:00:00
2018-06-21 09:00:00------当前时间
2018-06-21 12:00:00
2018-06-25 21:00:00

第四题：求出未来5天天气
1.打印每天的6:00,12:00,18:00的天气(城市,温度，情况，气压，最高温度，最低温度)
2.同上写出[英文版的]
3.根据天气的情况，给出建议：例如，今天下雨，提示带伞。今天温度高，穿衬衫...三个件以上
4.根据温度打印出问题折线图
    28——————————————————————————————
    30——————————————————————————————————
    10——————————————————
5.打印出其他10个城市的天气，计算出天气排名，按着大到小的顺序。



@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》list列表-》index 0 字典-》main字典-》temp变量
data['list'][0]['main']['temp']
#data字典-》list列表-》index 0 字典-》main字典-》temp_max变量

#data字典-》list列表-》index 0 字典-》main字典-》temp_min变量


import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)



msg(0)
msg(2)
msg(6)
msg(8)
msg(10)
msg(14)
msg(16)
msg(18)
msg(22)
msg(24)
msg(26)
msg(30)
msg(32)
msg(34)  
ls=

sorted(ls)

    
    
    ls=[]
hour=0
dt_txt=data['list'][hour]['dt_txt']
d11=print('{}{}的温度:{},天气情况:{},气压:{},最高温度:{},最低温度:{}'.format(city,dt_txt,temp,description,
          pressure,temp_max,temp_min)
ls=[]
hour=0
dt_txt=data['list'][hour]['dt_txt']
d11=print('{}{}的温度:{},天气情况:{},气压:{},最高温度:{},最低温度:{}'.format(city,dt_txt,temp,description,
          pressure,temp_max,temp_min)

d12=print('{}{}的温度:{},天气情况:{},气压:{},最高温度:{},最低温度:{}'.format(city,dt_txt,temp,description,
          pressure,temp_max,temp_min)
d13=print('{}{}的温度:{},天气情况:{},气压:{},最高温度:{},最低温度:{}'.format(city,dt_txt,temp,description,
          pressure,temp_max,temp_min)
print('建议：打伞，穿衣，预防感冒')
d21=print('{}{}的温度:{},天气情况:{},气压:{},最高温度:{},最低温度:{}'.format(city,dt_txt,temp,description,
          pressure,temp_max,temp_min)
d22=print('{}{}的温度:{},天气情况:{},气压:{},最高温度:{},最低温度:{}'.format(city,dt_txt,temp,description,
          pressure,temp_max,temp_min)
d23=print('{}{}的温度:{},天气情况:{},气压:{},最高温度:{},最低温度:{}'.format(city,dt_txt,temp,description,
          pressure,temp_max,temp_min)
print('建议：打伞，穿衣，预防感冒')
d31=print('{}{}的温度:{},天气情况:{},气压:{},最高温度:{},最低温度:{}'.format(city,dt_txt,temp,description,
          pressure,temp_max,temp_min)
d32=print('{}{}的温度:{},天气情况:{},气压:{},最高温度:{},最低温度:{}'.format(city,dt_txt,temp,description,
          pressure,temp_max,temp_min)
d33=print('{}{}的温度:{},天气情况:{},气压:{},最高温度:{},最低温度:{}'.format(city,dt_txt,temp,description,
          pressure,temp_max,temp_min)
print('建议：打伞，穿衣，预防感冒')
d41=print('{}{}的温度:{},天气情况:{},气压:{},最高温度:{},最低温度:{}'.format(city,dt_txt,temp,description,
          pressure,temp_max,temp_min)
d42=print('{}{}的温度:{},天气情况:{},气压:{},最高温度:{},最低温度:{}'.format(city,dt_txt,temp,description,
          pressure,temp_max,temp_min)
d43=print('{}{}的温度:{},天气情况:{},气压:{},最高温度:{},最低温度:{}'.format(city,dt_txt,temp,description,
          pressure,temp_max,temp_min)
print('建议：带伞，少外出，预防感冒')
d51=print('{}{}的温度:{},天气情况:{},气压:{},最高温度:{},最低温度:{}'.format(city,dt_txt,temp,description,
          pressure,temp_max,temp_min)
d52=print('{}{}的温度:{},天气情况:{},气压:{},最高温度:{},最低温度:{}'.format(city,dt_txt,temp,description,
          pressure,temp_max,temp_min)
d53=print('{}{}的温度:{},天气情况:{},气压:{},最高温度:{},最低温度:{}'.format(city,dt_txt,temp,description,
          pressure,temp_max,temp_min)
print('建议：带伞，少外出，预防感冒')
d1=print('{}{}temp:{},description:{},pressure:{},temp_max:{},temp_min:{}'.format(data['city']['name'],
      data['list'][0]['dt_txt'],
      data['list'][0]['main']['temp'],
      data['list'][0]['weather'][0]['main'],
      data['list'][0]['main']['pressure'],
      data['list'][0]['main']['temp_max'],
      data['list'][0]['main']['temp_min']))
d2=print('{}{}temp:{},description:{},pressure:{},temp_max:{},temp_min:{}'.format(data['city']['name'],
      data['list'][2]['dt_txt'],
      data['list'][2]['main']['temp'],
      data['list'][2]['weather'][0]['main'],
      data['list'][2]['main']['pressure'],
      data['list'][2]['main']['temp_max'],
      data['list'][2]['main']['temp_min']))
d3=print('{}{}temp:{},description:{},pressure:{},temp_max:{},temp_min:{}'.format(data['city']['name'],
      data['list'][4]['dt_txt'],
      data['list'][4]['main']['temp'],
      data['list'][4]['weather'][0]['main'],
      data['list'][4]['main']['pressure'],
      data['list'][4]['main']['temp_max'],
      data['list'][4]['main']['temp_min']))
d4=print('{}{}temp:{},description:{},pressure:{},temp_max:{},temp_min:{}'.format(data['city']['name'],
      data['list'][8]['dt_txt'],
      data['list'][0]['main']['temp'],
      data['list'][8]['weather'][0]['main'],
      data['list'][8]['main']['pressure'],
      data['list'][8]['main']['temp_max'],
      data['list'][8]['main']['temp_min']))
d5=print('{}{}temp:{},description:{},pressure:{},temp_max:{},temp_min:{}'.format(data['city']['name'],
      data['list'][10]['dt_txt'],
      data['list'][10]['main']['temp'],
      data['list'][10]['weather'][0]['main'],
      data['list'][10]['main']['pressure'],
      data['list'][10]['main']['temp_max'],
      data['list'][10]['main']['temp_min']))
d6=print('{}{}temp:{},description:{},pressure:{},temp_max:{},temp_min:{}'.format(data['city']['name'],
      data['list'][12]['dt_txt'],
      data['list'][12]['main']['temp'],
      data['list'][12]['weather'][0]['main'],
      data['list'][12]['main']['pressure'],
      data['list'][12]['main']['temp_max'],
      data['list'][12]['main']['temp_min']))
d7=print('{}{}temp:{},description:{},pressure:{},temp_max:{},temp_min:{}'.format(data['city']['name'],
      data['list'][16]['dt_txt'],
      data['list'][16]['main']['temp'],
      data['list'][16]['weather'][0]['main'],
      data['list'][16]['main']['pressure'],
      data['list'][16]['main']['temp_max'],
      data['list'][16]['main']['temp_min']))
d8=print('{}{}temp:{},description:{},pressure:{},temp_max:{},temp_min:{}'.format(data['city']['name'],
      data['list'][18]['dt_txt'],
      data['list'][18]['main']['temp'],
      data['list'][18]['weather'][0]['main'],
      data['list'][18]['main']['pressure'],
      data['list'][18]['main']['temp_max'],
      data['list'][18]['main']['temp_min']))
d9=print('{}{}temp:{},description:{},pressure:{},temp_max:{},temp_min:{}'.format(data['city']['name'],
      data['list'][20]['dt_txt'],
      data['list'][20]['main']['temp'],
      data['list'][20]['weather'][0]['main'],
      data['list'][20]['main']['pressure'],
      data['list'][20]['main']['temp_max'],
      data['list'][20]['main']['temp_min']))
d10=print('{}{}temp:{},description:{},pressure:{},temp_max:{},temp_min:{}'.format(data['city']['name'],
      data['list'][24]['dt_txt'],
      data['list'][24]['main']['temp'],
      data['list'][24]['weather'][0]['main'],
      data['list'][24]['main']['pressure'],
      data['list'][24]['main']['temp_max'],
      data['list'][24]['main']['temp_min']))
d11=print('{}{}temp:{},description:{},pressure:{},temp_max:{},temp_min:{}'.format(data['city']['name'],
      data['list'][26]['dt_txt'],
      data['list'][26]['main']['temp'],
      data['list'][26]['weather'][0]['main'],
      data['list'][26]['main']['pressure'],
      data['list'][26]['main']['temp_max'],
      data['list'][26]['main']['temp_min']))
d12=print('{}{}temp:{},description:{},pressure:{},temp_max:{},temp_min:{}'.format(data['city']['name'],
      data['list'][28]['dt_txt'],
      data['list'][28]['main']['temp'],
      data['list'][28]['weather'][0]['main'],
      data['list'][28]['main']['pressure'],
      data['list'][28]['main']['temp_max'],
      data['list'][28]['main']['temp_min']))
d13=print('{}{}temp:{},description:{},pressure:{},temp_max:{},temp_min:{}'.format(data['city']['name'],
      data['list'][32]['dt_txt'],
      data['list'][32]['main']['temp'],
      data['list'][32]['weather'][0]['main'],
      data['list'][32]['main']['pressure'],
      data['list'][32]['main']['temp_max'],
      data['list'][32]['main']['temp_min']))
d14=print('{}{}temp:{},description:{},pressure:{},temp_max:{},temp_min:{}'.format(data['city']['name'],
      data['list'][34]['dt_txt'],
      data['list'][34]['main']['temp'],
      data['list'][34]['weather'][0]['main'],
      data['list'][34]['main']['pressure'],
      data['list'][34]['main']['temp_max'],
      data['list'][34]['main']['temp_min']))
d15=print('{}{}temp:{},description:{},pressure:{},temp_max:{},temp_min:{}'.format(data['city']['name'],
      data['list'][36]['dt_txt'],
      data['list'][36]['main']['temp'],
      data['list'][36]['weather'][0]['main'],
      data['list'][36]['main']['pressure'],
      data['list'][36]['main']['temp_max'],
      data['list'][36]['main']['temp_min']))
def msg():
    




