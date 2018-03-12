from turtle import *

color('blue')
speed(-1)
shape('blank')

def square(dec,deg):
    for i in range(4):
        forward(300 - dec)
        right(90)
    right(deg)

left(220)
for i in range(50):
    square(6* i, 10)

mainloop()
