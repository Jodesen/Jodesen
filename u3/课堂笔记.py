#字符串处理
import time
print('字符串处理'.center(25,'='))
print('a出现的次数是:'+\
      str('(i have a pen.i hava a apple,emm,apple pen.'\
          .count('a')))#获取当前字符串某一值的重复次数    \可以换输代码

print('A,B,C,D'.split(','))  #将字符串变成数组
print(''.center(29,'='),'\n')

#获取时间
print('时间获取'.center(30,'='))
a=time.ctime()
b=time.gmtime()
print(a,'\n',b)
print('当前时间是:'+time.strftime('%Y年%m月%d日 %H点%M分%S秒',time.gmtime()))
print(''.center(33,'='),'\n')

#获取cpu时间
print('读取CPU时间'.center(23,'='))
c=time.perf_counter()
time.sleep(2)
e=time.perf_counter()
print('程序运行{:.2f}秒'.format(e-c))   #两次获取时间做差
print(''.center(26,'='),'\n')


#多行进度条
jingdu=10
print('进度条执行开始'.center(20,'='))
for i in range(11):
    a='*'*i
    b='.'*(jingdu-i)
    c=(i/jingdu)*100
    print(' {:^3.0f}%[{}->{}]'.format(c,a,b))
    time.sleep(0.1)
print('执行结束'.center(20,'='))


#单行进度条
for i in range(101):
    print('\r{:3}%'.format(i),end='')
    time.sleep(0.1)
print('加载成功')