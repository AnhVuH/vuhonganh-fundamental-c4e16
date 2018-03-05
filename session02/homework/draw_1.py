from turtle import *

color("red")
def draw(deg):
    left(deg)
    left(30)
    forward(100)
    right(60)
    forward(100)
    right(120)
    forward(100)
    right(60)
    home()

for  i in range(0,360,90):
    draw(i)

mainloop()
