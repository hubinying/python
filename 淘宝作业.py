# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:03:05 2018

@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?q=%E7%94%B7%E8%A3%A4&imgfile=&js=1&stats_click=search_radio_all:1&initiative_id=staobaoz_20180624&ie=utf8&loc=%E5%8C%97%E4%BA%AC&bcoffset=3&ntoffset=3&p4ppushleft=1,48&s={}&ajax=true '
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
import urllib.request as r#导入联网工具包，命令为r
for i in range(1,4400,44):
    url='https://s.taobao.com/search?q=%E7%94%B7%E8%A3%A4&imgfile=&js=1&stats_click=search_radio_all:1&initiative_id=staobaoz_20180624&ie=utf8&loc=%E5%8C%97%E4%BA%AC&bcoffset=3&ntoffset=3&p4ppushleft=1,48&s={}&ajax=true '.format(i)
    import json
    data=json.loads(data)
    for t in range(44):
        a=data['mods']['itemlist']['data']['auctions'][t]['raw_title'],
        b=data['mods']['itemlist']['data']['auctions'][t]['view_price'],
        c=data['mods']['itemlist']['data']['auctions'][t]['view_sales'],
        d=data['mods']['itemlist']['data']['auctions'][t]['item_loc'],
        e=data['mods']['itemlist']['data']['auctions'][t]['nick'],
        f=open('./b.csv','a').write('{},{},{},{},{}\n'.format(a,b,c,d,e))
        if len(data['mods']['itemlist']['data']['auctions'][t])==20:
            continue
        f
for i in range(100):
    if i>=3:
        q=i*44
        import urllib.request as r#导入联网工具包，命令为r
        url='https://s.taobao.com/search?q=t%E6%81%A4%E7%94%B7&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180625&ie=utf8&loc=%E5%8C%97%E4%BA%AC&ajax=true'
        data=r.urlopen(url).read().decode('utf-8')
        import json
        data=json.loads(data)
        def p(t):
             a=data['mods']['itemlist']['data']['auctions'][t]['raw_title']
             b=data['mods']['itemlist']['data']['auctions'][t]['view_price']
             c=data['mods']['itemlist']['data']['auctions'][t]['view_sales']
             d=data['mods']['itemlist']['data']['auctions'][t]['item_loc']
             e=data['mods']['itemlist']['data']['auctions'][t]['nick']
             f=open('./c.csv','a')
             f.write('{},{},{},{},{}\n'.format(a,b,c,d,e))
             f.close()
             for t in range(44):
                 if len(data['mods']['itemlist']['data']['auctions'][t])==20:
                     continue
                 s(t)

import urllib.request as r
for i in range(1,4400,44):
    url='https://s.taobao.com/search?q=%E7%94%B7%E8%A3%A4&imgfile=&js=1&stats_click=search_radio_all:1&initiative_id=staobaoz_20180624&ie=utf8&loc=%E5%8C%97%E4%BA%AC&bcoffset=3&ntoffset=3&p4ppushleft=1,48&s={}&ajax=true '.format(i)
    data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
for t in range(44):
    a=data['mods']['itemlist']['data']['auctions'][t]['raw_title'],
    b=data['mods']['itemlist']['data']['auctions'][t]['view_price'],
    c=data['mods']['itemlist']['data']['auctions'][t]['view_sales'],
    d=data['mods']['itemlist']['data']['auctions'][t]['item_loc'],
    e=data['mods']['itemlist']['data']['auctions'][t]['nick'],
    f=open('./b.csv','a').write('{},{},{},{},{}\n'.format(a,b,c,d,e))

import urllib.request as r
f=open('./f.csv','a')
for i in range(0,4400,44):
     url='https://s.taobao.com/search?q=t%E6%81%A4%E7%94%B7&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&loc=%E5%B9%BF%E5%B7%9E&s={}&ajax=true'.format(i)
     data=r.urlopen(url).read().decode('utf-8')
     import json
     data=json.loads(data)
     for t in range(36):
         a=data['mods']['itemlist']['data']['auctions'][t]['raw_title']
         b=data['mods']['itemlist']['data']['auctions'][t]['view_price']
         c=data['mods']['itemlist']['data']['auctions'][t]['view_sales']
         d=data['mods']['itemlist']['data']['auctions'][t]['item_loc']
         e=data['mods']['itemlist']['data']['auctions'][t]['nick']
         f.write('{},{},{},{},{}\n'.format(a,b,c,d,e))




f=open('./hangzhou.csv','w')
f.write('店铺名,商品名,价格,销量,地址\n')
for i in range(0,100):
    import urllib.request as r
    url2='https://s.taobao.com/search?q=t%E6%81%A4%E7%94%B7&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&loc=%E5%B9%BF%E5%B7%9E&s=0&ajax=true '
    a=44*i
    url=url2.replace('0&ajax=true',str(a)+'&ajax=true')
    data=r.urlopen(url).read().decode('utf-8')
    import json
    data=json.loads(data)
    l=len(data['mods']['itemlist']['data']['auctions'])
    for a in range(0,l):
        nick=data['mods']['itemlist']['data']['auctions'][a]['nick']#店铺名
        raw_title=data['mods']['itemlist']['data']['auctions'][a]['raw_title']#商品名
        view_price=data['mods']['itemlist']['data']['auctions'][a]['view_price']#价格
        view_sales=data['mods']['itemlist']['data']['auctions'][a]['view_sales']#销量
        item_loc=data['mods']['itemlist']['data']['auctions'][a]['item_loc']#地址
        f.write('{},{},{},{},{}\n'.format(nick,raw_title,view_price,view_sales,item_loc))
    print('第{}页已获取数据'.format(i+1))
f.close()
























