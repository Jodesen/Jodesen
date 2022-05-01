# -*- coding = utf-8 -*-
# @Time : 2021/4/18 16:08
# @Author :Xu
# @File : 自动轨迹绘制.py
# @Software: PyCharm

import turtle as t
t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pencolor('red')
t.pensize(5)
#数据获取
data = []
f = open("data.txt",encoding='UTF-8')
for line in f:
    line = line.replace("\n","")
    data.append(list(map(eval,line.split(","))))
f.close()
#自动绘制
for i in range(len(data)):
    t.pencolor(data[i][3],data[i][4],data[i][5])
    t.fd(data[i][0])
    if data[i][1]:
        t.right(data[i][2])
    else:
        t.left(data[i][2])

