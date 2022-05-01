#单行动态进度条改进版
import time
jingdu=50
print('进度条执行开始'.center(jingdu//2,'-'))
star = time.perf_counter()  #获取cpu时间
for i in range(jingdu+1):
    a='*'*i
    b='.'*(jingdu-i)
    c=(i/jingdu)*100
    dur = time.perf_counter()-star   #时间差值得出程序运行时间
    print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur),end='')
    time.sleep(0.1)
print('\n'+'执行结束'.center(jingdu//2,'-'))