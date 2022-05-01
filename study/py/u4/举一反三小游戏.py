import random,time
a=eval(input('请输入1进入游戏:'))
if a==1:
    b='石头','剪刀','布'
    print('1 [石头],2 [剪刀],3 [布]')
    e=eval(input('请输入对应数字:'))
    c=b[e - 1]
    time.sleep(0.5)

    d = random.randint(1,3)
    if e==d:
        print('你出的是:',c)
        print('我出的是:',b[d - 1])
        print('平局了')
    elif d == 1 and c == 2:
        print('你出的是:', c)
        print('我出的是:', b[d - 1])
        print('我赢了')
    elif d == 1 and  c == 3:
        print('你出的是:', c)
        print('我出的是:', b[d - 1])
        print('你赢了')
    elif d == 2 and  c == 1:
        print('你出的是:', c)
        print('我出的是:', b[d - 1])
        print('你赢了')
    elif d == 2 and  c == 3:
        print('你出的是:', c)
        print('我出的是:', b[d - 1])
        print('我赢了')
    elif d == 3 and  c == 1:
        print('你出的是:', c)
        print('我出的是:', b[d - 1])
        print('我赢了')
    elif d == 3 and c == 2:
        print('你出的是:', c)
        print('我出的是:', b[d - 1])
        print('你赢了')

    print('你出的是:', c)
    print('我出的是:', b[d - 1])
else:
    print('退出中')


