# -*- coding = utf-8 -*-
# @Time : 2021/4/21 17:56
# @Author :Xu
# @File : 词云.py
# @Software: PyCharm

# 使用默认方式生成词云
# import jieba
# import wordcloud
# f = open('新时代中国特色社会主义.txt','r',encoding='utf-8')
# t = f.read()
# f.close()
# ls = jieba.lcut(t)
# txt = ' '.join(ls)
# w = wordcloud.WordCloud(\
#     width = 1000, height = 700,\
#     background_color = "white",
#     font_path = "msyh.ttc"
#     )
# w.generate(txt)
# w.to_file('新时代中国特色社会主义.png')
# print(ls)

#利用其它图形生成云词
import jieba
import wordcloud
from imageio import imread
mask = imread('五角星.png')
f = open('新时代中国特色社会主义.txt','r',encoding='utf-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = ' '.join(ls)
w = wordcloud.WordCloud(\
    width = 1000, height = 700,\
    background_color = "white",\
    font_path = "msyh.ttc", mask = mask\
    )
w.generate(txt)
w.to_file('新时代中国特色社会主义.png')
print(ls)


