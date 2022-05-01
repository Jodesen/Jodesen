# -*- coding = utf-8 -*-
# @Time : 2021/4/21 11:15
# @Author :Xu
# @File : wordcloud库.py
# @Software: PyCharm
'''
w.generate(txt)         向wordcould对像w中加载文本txt
w.to_file(filename)     将词云输出为图像文件，png或jpg格式
width                   指定词云对象生成图片的宽度，默认400像素
height                  指定词云对象生成图片的高度，默认200像素
min_font_size           指定词云中字体的最小字号，默认4号
max_font_size           指定词云中字体的最大字号，根据高度自动调节
font_step               指定词云中字体字号的步进间隔，默认为1
font_path               指定字体文件的路径，默认None
font_words              指定词云显示的最大单词数量，默认200
stop_words              指定词云的排除词列表

mask                    指定词云形状，默认为长方形，需要引用imread()函数
                        from scipy.misc import imread
                        mk=imread('pic.png')
                        wwordcloud.WordCloud(mask=mk)

background_color        指定词云图片的背景颜色，默认黑色
'''

import wordcloud
import jieba
#使用实例
# c = wordcloud.WordCloud()
# c.generate('wordcloud by python')
# c.to_file('pywordcloud.png')

#设置背景颜色例子
# txt = 'life is short,you need study python'
# w = wordcloud.WordCloud(\
#     background_color='white')
# w.generate(txt)
# w.to_file('123.png')
txt = "程序设计语言是计算机能够理解和\
识别用户操作意图的一种交互体系，它按照\
特定规则组织计算机指令，使计算机能够自\
动进行各种运算处理。"
w = wordcloud.WordCloud(width=1000,font_path='msyh.ttc',height=700)
w.generate(' '.join(jieba.lcut(txt)))
w.to_file('worcloud.png')
