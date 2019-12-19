# -*- coding: utf-8 -*-
import requests

r = requests.get('https://www.baidu.com/') # 百度首页

# 带参数写法： 传入一个dict作为params参数
#r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
#  地址为： 'https://www.douban.com/search?q=python&cat=1001'

#需要传入HTTP Header时，我们传入一个dict作为headers参数：
#r = requests.get('https://www.baidu.com/',headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})

r.status_code

r.encoding
#print(r.encoding)

r.content
#print(r.content)
str = str(r.content)#转换为字符串，进行写入保存

r.text
#print(r.text)

#定义文件路径
fpath = 'E:/py/baidu_index.html'

with open(fpath, 'w') as f:
    f.write(str)

with open(fpath, 'r') as f:
    s = f.read()
    print(s)
