from turtle import color, shape, speed, forward, left, mainloop

color('blue')
shape('blank')
speed(100)

def square(deg):
    for i in range(4):
        for j in range(4):
            forward(100)
            left(90)
        left(90)
    left(deg)

for i in range(6):
    square(15)

mainloop()
