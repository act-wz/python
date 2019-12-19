# -*- coding: utf-8 -*-

#test I/O (读写文件)
from datetime import datetime #Python处理日期和时间的标准库

#注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数
now = datetime.now() # 获取当前datetime
print(now)

gs_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')#时间格式输出
print(gs_time)

dt = datetime(2018, 8, 8, 6, 6,6) # 用指定日期时间创建datetime
print(dt)#输出结果为：2018-08-08 06:06:06

timestamp = dt.timestamp()  # 把datetime转换为timestamp 时间戳
print(timestamp)

#定义文件路径
fpath = 'E:/py/test.txt'

#打开文件
f = open(fpath, 'r')

#读文件
with open(fpath, 'r') as f:
    r = f.read()
    print(r)

# for line in f.readlines():
#    print(line) #读单行
#    print(line.strip()) # 把末尾的'\n'删掉


#写文件  tips:注意写入会覆盖之前的文本
#追加到文件末尾可以传入'a'以追加（append）模式写入
with open(fpath, 'w') as f:
    f.write('Hello, world!')

with open(fpath, 'r') as f:
    s = f.read()
    print(s)
    print(s.strip())#加换行

with open(fpath, 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))#时间格式输出

with open(fpath, 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open(fpath, 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)

