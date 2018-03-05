from turtle import *
shape('turtle')
speed (-1)
color('green')

num = int(input("so canh:"))

fillcolor("red")

begin_fill()

for i in range(num):
    forward(50)
    left(360/num)

end_fill()
mainloop()
