# -*- coding = utf-8 -*-
# @Time : 2021/4/24 15:02
# @Author :Xu
# @File : os库的使用.py
# @Software: PyCharm

'''
os.path.abspath(path)           返回path在当前系统中的绝对路径
os.path.normpath(path)          归一化path的表现形式，统一用\\分割路径
os.path.relpath(path)           返回当前程序与文件之间的相对路径(relative path)
os.path.dirname(path)           返回path中的目录名称
os.path.basename(path)          返回path中最后的文件名称
os.path.join(path,*paths)       组合path与paths，返回一个路径字符串
os.path.exists(path)            判断path对应文件或目录是否存在，返回True或False
os.path.isfile(path)            判断path所对应是否为已存在的文件，返回True或False
os.path.isdir(path)             判断path所对应是否为已存在的目录，返回True或False
os.path.getatime(path)          返回path对应文件或目录上一次的访问时间
os.path.getmtime(path)          返回path对应文件或目录最近一次的修改时间
os.path.getctime(path)          返回path对应文件或目录的创建时间
os.path.getsize(path)           返回path对应文件的大小，以字节为单位
os.chdir(path)                  修改当前程序的操作路径
os.getcwd()                     返回程序的当前路径
os.getlogin()                   获得系统登陆用户名称
os.cpu_count()                  获得当前系统的CPU数量
'''


import os
# os.system("C:\\Windows\\System32\calc.exe") #打开计算器
print(os.cpu_count() )

