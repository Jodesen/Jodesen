'''基本思路
步骤一:绘制单格数字对应的数码管
步骤二:获得一串数字,绘制对应的数码管
步骤三:后的当前系统时间,绘制对应的数码管'''

import turtle,time
def drawgap():
    turtle.penup()
    turtle.fd(5)

def drawline(draw):#绘制单段数码管
    drawgap()
    turtle.pendown()if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)

def drawdigit(digit):#根据数字绘制数码管
    drawline(True)if digit in[2,3,4,5,6,8,9] else drawline(False)
    drawline(True)if digit in[0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.penup()#为绘制后续数字确定位置
    turtle.fd(20)#为绘制后续数字确定位置

def drawdate(date):#获得需要输出的数字  #date为日期,格式为 '%Y-%m=%d+'
    turtle.pencolor('red')
    for i in date:
        if i =='-':
                turtle.write('年',font=('Arial',18,'normal'))
                turtle.pencolor('green')
                turtle.fd(40)
        elif i =='=':
                turtle.write('月',font=('Arial',18,'normal'))
                turtle.pencolor('blue')
                turtle.fd(40)
        elif i =='+':
                turtle.write('日', font=('Arial', 18, 'normal'))
        else:
                drawdigit(eval(i))



def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawdate(time.strftime('%Y-%m=%d+',time.gmtime()))
    turtle.hideturtle()
    turtle.done()
main()