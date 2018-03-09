from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

def draw_poly(n):
    color(colors[n-3])
    for i in range(n):
        forward(100)
        left(360/n)
for i in range(3,8):
    draw_poly(i)

mainloop()
