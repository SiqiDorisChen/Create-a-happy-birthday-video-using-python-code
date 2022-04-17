# If you cannot run me successfully, try the following line to install 'turtle'
# pip3 install turtle

import turtle as t
from turtle import *
import random as r

n = 100.0

speed(1500)
pensize(5)
screensize(800, 800, bg='black')
left(90)
forward(250)
color("orange", "yellow")
begin_fill()
left(126)

for i in range(5):
    forward(n / 5)
    right(144)
    forward(n / 5)
    left(72)
end_fill()
right(126)


backward(50)

for i in range(20):
    a = 200 - 400 * r.random()
    b = 10 - 20 * r.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()
    if r.randint(0, 1) == 0:
        color('tomato')
    else:
        color('wheat')
    circle(2)
    up()
    backward(a)
    right(90)
    backward(b)

def drawsnowman(n,m,a,b):
    t.goto(n, m)
    t.pencolor("white")
    t.pensize(2)
    t.fillcolor("white")
    t.seth(0)
    t.begin_fill()
    t.circle(a)
    t.end_fill()
    t.seth(180)
    t.begin_fill()
    t.circle(b)
    t.end_fill()
    t.pencolor("black")
    t.fillcolor("black")
    t.penup()
    t.goto(n-a/4, m+a)
    t.seth(0)
    t.pendown()
    t.begin_fill()
    t.circle(2)
    t.end_fill()
    t.penup()
    t.goto(n+a/4, m+a)
    t.seth(0)
    t.pendown()
    t.begin_fill()
    t.circle(2)
    t.end_fill()
    t.penup()
    t.goto(n, m+a/2)
    t.seth(0)
    t.pendown()
    t.fd(5)
    t.penup()
    t.pencolor("red")
    t.fillcolor("red")
    t.goto(n, m-b/4)
    t.pendown()
    t.begin_fill()
    t.circle(2)
    t.end_fill()
    t.penup()
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.goto(n, m-b/2)
    t.pendown()
    t.begin_fill()
    t.circle(2)
    t.end_fill()
    t.penup()
    t.pencolor("orange")
    t.fillcolor("orange")
    t.goto(n, m-(3*b)/4)
    t.pendown()
    t.begin_fill()
    t.circle(2)
    t.end_fill()

drawsnowman(-200, -200, 20, 30)
drawsnowman(-250, -200, 30, 40)


def drawsnow():
    t.ht()
    t.pensize(4)
    for i in range(40):
        t.pencolor("white")
        t.pu()
        t.setx(r.randint(-350, 350))
        t.sety(r.randint(-100, 350))
        t.pd()
        dens = 6
        snowsize = r.randint(1, 10)
        for j in range(dens):
            t.fd(int(snowsize))
            t.backward(int(snowsize))
            t.right(int(360 / dens))

drawsnow()
t.up()
t.goto(100, 100)
t.down()
t.color("dark red", "red")
t.penup()
t.write("XXXXX", font=("Comic Sans MS", 35, "bold"))
t.end_fill()

t.goto(100, 5)
t.down()
t.color("dark red", "red")
t.penup()
t.write("Happy Birthday!", font=("Comic Sans MS", 30, "bold"))
t.end_fill()

t.done()
