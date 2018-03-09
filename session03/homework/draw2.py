from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

def rectangle(n):
    color(colors[n])
    filling()
    begin_fill()
    for i in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    end_fill()
    forward(50)

for i in range(5):
    rectangle(i)

mainloop()
