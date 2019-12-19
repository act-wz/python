# -*- coding: utf-8 -*-
# 定义一个函数要使用def语句，
# 依次写出函数名、括号、括号中的参数和冒号:
# tips：求绝对值的函数abs，在交互式命令行通过help(abs)查看abs函数的帮助信息
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))

#如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass

#代码实例：
# import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。
import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

n = my_abs(-20)
print(n)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)