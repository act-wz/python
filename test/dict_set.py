# -*- coding: utf-8 -*-
# 1. dict全称dictionary，在其他语言中也称为map
# 使用键-值（key-value）存储(类比数组、JSON)
# dict的key必须是不可变对象
names = ['A', 'B', 'C']
scores = [95, 75, 85]

d = {'A': 95, 'B': 75, 'C': 85}
# dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
d.get('A')
d.get('D',-1)
print(d.get('D',-1))
# tips：返回None的时候Python的交互环境不显示结果。

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('B')
print(d)


# 2. set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
# 通过add(key)方法可以添加元素到set中，通过remove(key)方法可以删除元素
# tips:可以重复添加，但不会有效果(重复元素在set中自动被过滤)：
s = set([1, 1, 2, 2, 3, 3])
print(s)
s.add(4)
s.remove(1)
print(s)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作:
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
#交集：s1 & s2 =》{2, 3}
#并集：s1 | s2 =》{1, 2, 3, 4}