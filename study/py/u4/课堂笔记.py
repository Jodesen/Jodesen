# #单分支结构
# guess=eval(input())
# print(('猜{}了'.format('对'if guess==99 else'错')))
# # 多分支结构
# score=eval(input())
# if score >=90:
#     grade="A"
# elif score>=80:
#     grade="B"
# elif score>=70:
#     grade="C"
# elif score>=60:
#     grade="D"
# else:
#     grade='E'
# print('输入的成绩属于 {} 等'.format(grade))
# # 程序异常处理
# try :
#     num=eval(input('请输入一个整数:'))
#     print(num**2)
# except NameError :
#     print('输入格式错误')

#程序循环结构
# for i in range(1,10,2):
#     print(i)
# for c in 'Python123':
#     print(c,end=',')
# for item in [123,'PY',456]: #列表遍历循环
#     print(item,end=' ')

# for line in fi:   文件遍历循环
#     <语句块>

#无限循环
# a=3
# while a>0:
#     a-=1
#     print(a)

# #循环结构
# a='PYTHON'
# for c in a:  #跳过当次循环
#     if c=='T':
#         continue
#     print(c,end='')
#
# while a!='':  #删去了最后一个字符
#     for c in a:
#         print(c,end=' ')
#     a = a[:-1]
# #else与循环结合,当循环正常执行后.else作为奖励语句,反之,else后的语句则不会执行
#
#
#random 随机
'''import random
#seed 初始化给定的随机数种子,默认为当前系统时间
#random()生成[0.0,1.0]之间的随机小数
rando的扩展函数
randint(a,b)        生成一个[a,b]之间的整数
randrange(m,n[k])   生成一个[m,n]之间以K为步长的随机整数
getrandbits(k)      生成一个K比特长的随机整数
uniform(a,b)        生成一个[a,b]之间的随机小数
choice(序列)         从序列中随机选择一个元素
shuffle(序列)        将序列随机排序后,返回打乱后的序列
'''
# #圆周率计算
# from random import random
# from time import perf_counter
# DARTS = 1000*1000
# hits = 0.0
# start = perf_counter()
# for i in range(1,DARTS+1):
#     x,y = random(),random()
#     dist = pow(x**2+y**2,0.5)
#     if dist <= 1.0:
#         hits+=1
# pi = 4 * (hits/DARTS)
# print("圆周率值是:{}".format(pi))
# print("运行时间是:{:.5f}s".format(perf_counter()-start))

#水仙花数
# s = ""
# for i in range(100, 1000):
#     t = str(i)
#     if pow(eval(t[0]),3) + pow(eval(t[1]),3) + pow(eval(t[2]),3) == i :
#         s += "{},".format(i)#将I填充进去
# print(s[:-1])#输出第一位到最后一位为止的数

'''三次登录验证
count = 0
while count < 3:
    name = input()
    password = input()
    if name == 'Kate'and password == '666666':
        print("登录成功！")
        break
    else:
        count += 1
        if count == 3:
            print("3次用户名或者密码均有误！退出程序。")
'''
a = 2
for i in range(3,100):
    for b in range(2,i):
        if i%b == 0:
            break
    else:
        a += i
print(a)

num=[]
i=2
for i in range(2,100):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)