from turtle import *

def draw(n):
    if n %2 != 0:
        color("blue")
    else:
        color("red")
    for i in range(n):
        forward(100)
        left(360/n)
for i in range(3,7):
    draw(i)
mainloop()
