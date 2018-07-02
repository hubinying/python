# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 16:29:55 2018

@author: Administrator
"""

print('火车站三字码是：'+'BJX')

"""
    ls=open('./火车站编码.csv','r').readlines()
UnicodeDecodeError: 'gbk' codec can't decode byte 0xf8 in position 6572: illegal multibyte sequence
"""
def hanzi_to_pin(s):
    ls=open('./火车站编码.csv','r',encoding='utf-8').readlines()
    #开发思路，首先拿到全部的火车站列表-》循环比对是否有 某个火车站(.split(',')[0])，找到之后，[1]
    abc=''
    for i in ls:
        if s==i.split(',')[0]:
            abc=i.split(',')[1]
            break
    return abc

import urllib.request as r#导入联网工具包，命令为r
dat=input('请输入年月日')
from_station=input('出发站')#北京
from_station=hanzi_to_pin(from_station)
to_station=input('到达站')#成都
to_station=hanzi_to_pin(to_station)
print(dat,from_station,to_station)
#https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-17&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=NJH&purpose_codes=0X00
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'
url=url.format(dat,from_station,to_station).replace('\n','')
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
l=data['data']['result']
p='  '
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for i in title:
    print(i.center(11),end='')
print()
ls1=[]
ls2=[]
l=len(data['data']['result'])
for a in range(l):
    s=data['data']['result'][a]
    ls=s.split('|')
    if ls[3].startswith('{}'.format(ls[3])):
        ls[6]=data['data']['map'].get('{}'.format(ls[6]))
        ls[7]=data['data']['map'].get('{}'.format(ls[7]))
        if ls[0]=='':
            ls[1]=('不能预订')
        la=[ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],ls[32],ls[31],ls[30],ls[21],ls[23],ls[33],ls[28],'--',ls[29],ls[26],'--',ls[1]]
        for b in la:
            if b=='':
                b='--'
                print(str(b).center(14).replace('[','(').replace(']',')'),end='')
            else:
                print(str(b).center(14).replace('[','(').replace(']',')'),end='')
    ls1.append(ls[10])
    ls2.append(ls[8])
sorted(ls1)
sorted(ls2)
print('\n')
print('程序结束')
