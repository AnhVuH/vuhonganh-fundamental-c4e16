from turtle import *

color('blue')
speed(-1)
shape('blank')

def square(dec,deg):
    for i in range(4):
        forward(5 + dec)
        left(90)
    left(deg)

for i in range(50):
    square(5* i, 10)

mainloop()
