#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

#创建html 字符串
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html)#创建 beautifulsoup 对象

#soup = BeautifulSoup(open('index.html')) #打开本地 HTML 文件来创建对象

#print(soup.prettify())#打印一下 soup 对象的内容，格式化输出

#分别获取html 标签
#   tips:  soup加标签名 轻松地获取这些标签的内容
# print(soup.title)
# print(soup.head)
# print(soup.a)
# print(soup.p)

#获取对象属性  name 和 attrs
# print (soup.a.name)

print(soup.a.get('href'))#get 方法获取标签属性值

print (soup.a.attrs)

#对标签 属性和内容等等 进行 操作
# soup.p['class']="newClass"#修改class
# del soup.p['class']#删除class
# print(soup.p)

# 获取标签内 内容
# 注意：如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。
# 如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容
# 如果tag包含了多个子节点,tag就无法确定，string 方法应该调用哪个子节点的内容, .string 的输出结果是 None
print (soup.p.string)

# 关于节知识
#tag 的 .content 属性可以将tag的子节点以列表的方式输出
#print (soup.head.contents)
#print (soup.body.contents)

# 遍历获取所有子节点
# for child in soup.body.children:
#   print (child)

# 判断类型是否为注释
if type(soup.a.string)== 'bs4.element.Comment':
  print (soup.a.string)

