# -*- coding = utf-8 -*-
# @Time : 2021/4/18 17:31
# @Author :Xu
# @File : 五星红旗.py
# @Software: PyCharm
import turtle
def WX():
  for i in range(5):
    turtle.fd(17)
    turtle.right(72)
    turtle.fd(17)
    turtle.left(144)
def wx():
    for i in range(5):
        turtle.fd(4)
        turtle.right(72)
        turtle.fd(4)
        turtle.left(144)
def FX():
    turtle.fd(300)
    turtle.right(90)
    turtle.fd(200)
    turtle.right(90)
    turtle.fd(300)
    turtle.right(90)
    turtle.fd(200)
def main():
  turtle.setup(600,400)
  turtle.penup()
  turtle.fd(-200)
  turtle.down()
  turtle.fillcolor("red")
  turtle.begin_fill()
  FX()
  turtle.end_fill()
  turtle.penup()
  turtle.seth(-55)
  turtle.fd(42)
  turtle.pencolor("yellow")
  turtle.pensize(1)
  turtle.down()
  turtle.fillcolor("yellow")
  turtle.begin_fill()
  turtle.seth(-36)
  WX()
  turtle.end_fill()
  turtle.penup()
  turtle.seth(20)
  turtle.fd(50)
  for i in range(4):
    turtle.penup()
    turtle.circle(-25,40)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    wx()
    turtle.end_fill()
  turtle.hideturtle()
  turtle.done()
main()