#第四个问题
def up(df):  #定义函数运算
    up=1
    for i in range(365):
        if i % 7 in [6,0]:
            up=up*(1-0.01)
        else:
            up=up*(1+df)
    return up##
bianliang = 0.01
while up(bianliang)<37.78:
    bianliang+=0.001
print('工作日的努力是:{:.3f}'.format(bianliang))
