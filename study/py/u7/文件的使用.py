# -*- coding = utf-8 -*-
# @Time : 2021/4/17 16:23
# @Author :Xu
# @File : 文件的使用.py
# @Software: PyCharm
'''打开模式
f= open('f.txt')            文本形式、只读模式、默认值
f= open('f.txt','rt')       文本形式、只读模式、同默认值
f= open('f.txt'.'w')        文本形式、覆盖写模式
f= open('f.txt','a+')       文本形式、追加写模式+读文件
f= open('f.txt','x')        文本形式、创建写模式
f= open('f.txt','b')        二进制形式、只读模式
f= open('f.txt','wb')       二进制形式、覆盖读写模式
'''
#<变量名>.close() 关闭模式
'''文件内容的读取
<f>.read(size=-1)           读取全部内容，如果给出参数，读入前size长度
<f>.readline(size=-1)       读入一行内容，如果给出参数，读入该行前size
<f>.readlines(hint=-1)      读入文件所有行，以每行为元素形成列表，如果给出参数，读入前hint行
'''
'''数据的文件写入
<f>.write(s)            向文件写入一个字符串或字节流
<f>.writelines(lines)   将一个元素全为字符串的列表写入文件
<f>.seek(offset)        改变当前文件操作指针的位置，offset参数0-文件开头  1-当前位置 2-文件结尾
'''