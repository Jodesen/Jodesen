# -*- codeing = utf-8 -*-
# @time : 2021/11/6 10:54
# @Author : Xu
# @File : 学爬.py
# @software : PyCharm

# a = input("输入:")
# print(type(int(a)))
# print("以下是一张用for循环语句写的乘法口诀表：")
# i=1
# j=1
# s=0
for i in range(1,10):           #第一行到第9行
    for j in range(1,i+1):    #第一列到第i列
        s=i*j
        print("{} * {} = {}".format(j,i,s),end="\t")  #打印输出


# r = 1
# s = 0
# while r <10:
#     c = 1
#     while c<r+1:
#         s=r*c
#         print("%d * %d = %d "%(c,r,s),end = "\t")
#         c+=1
#     print(" "*30)
#     r+=1

