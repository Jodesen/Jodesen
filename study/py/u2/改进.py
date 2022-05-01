from turtle import*
setup(650,350)
penup()
fd(-250)
pendown()
pensize(25)
pencolor('red')
seth(-40)
for i in range(4):
    circle(40,80)
    circle(-40,80)
circle(40,80/2)
fd(40)
circle(16,180)
fd(40*2/3)

for i in range(5):
    print('hello:',i)
done()