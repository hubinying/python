# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:59:33 2018

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=&tn=48021271_13_hao_pg&bar=&wd=python&rn=&oq=&rsv_pq=d2317f5600053ae6&rsv_t=bae5LaueFmwD9jXTehzXAgwPTN6p3uufUsNVBIOD%2BBANfCxAeQz4e6ZEPYG%2FFgtQxYzPgxzyt%2FEX&rqlang=cn'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls=re.compile('"title":"(.*?)"').findall(data)
ls1=re.compile('href="(.*?)" ').findall(data)
pl='<div class="c-abstract">(.*?)</div>'
ls2=re.compile(pl).findall(data)
for i in range(12):
    print('标题:{}\n,网址:{}\n,介绍:{}\n'.format(ls[i],ls1[i],ls2[i]))

