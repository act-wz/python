# -*- coding: utf-8 -*-
#if else
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

#循环
# 1、for...in循环
# (实例1：数组取值)
# 执行这段代码，会依次打印names的每一个元素
names = ['A', 'B', 'C']
for name in names:
    print(name)

#（实例2：高斯算法）
# tips： range(101)就可以生成0-100的整数序列
#如：list(range(5)) 等同于 [0, 1, 2, 3, 4]
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# 2、while循环，只要条件满足，就不断循环，条件不满足时退出循环
# 计算100以内所有奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# tips：Ctrl+C退出程序或者强制结束Python进程。（比喻退出死循环）
