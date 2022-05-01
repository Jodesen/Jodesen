# -*- codeing = utf-8 -*-
# @time : 2021/11/8 15:29
# @Author : Xu
# @File : try.py
# @software : PyCharm
# n=6
# for i in range(1,n+1):
# 	print('{}*6={}'.format(i,i*n),end=' ')
for n in range(1,10):
    for i in range(1, n+1):
        print('%d X %d = %d' % (i, n, i * n), end="\t")
    print('')
    n +=1
