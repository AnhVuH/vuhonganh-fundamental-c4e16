from turtle import *
import turtle
sc = turtle.Screen()
sc.bgcolor("green")
sc.title("star & clock")

a = turtle.Turtle()
a.shape("blank")
a.color("black")
a.pensize(5)

b = turtle.Turtle()
b.shape("turtle")
b.color("pink")
b.pensize(10)

a.penup()
a.setpos(100, 100)
a.pendown()
a.fillcolor("blue")
a.begin_fill()
for i in range(5):
    a.forward(100)
    a.right(144)
    a.forward(100)
a.end_fill()
b.penup()
b.setpos(-100, -100)

b.stamp()
for i in range(12):

    b.forward(100)
    b.stamp()
    b.backward(100)
    b.left(-30)


mainloop()
