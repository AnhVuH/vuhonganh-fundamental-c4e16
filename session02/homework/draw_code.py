def draw_c(size, row):
    if row == 0 or row == size -1:
        print("* " * size, end ="")
    else:
        print("* ",end = "  " * (size-1))
    print(end =" " * size )
def draw_o(size, row):
    if row == 0 or row == size -1:
        print("* " * size, end ="")
    else:
        print("* "+"  "*(size-2),end ="* ")
    print(end =" " * size)
def draw_d(size,row):
    if row == 0 or row == size -1:
        print("* " * (size-1), end ="  ")
    else:
        print("* "+"  " * (size-2), end ="* ")
    print(end =" " * size)
def draw_e(size,row):
    if row == 0 or row == size -1:
        print("* " * size, end ="")
    else:
        if row == (size//2):
            print("* " * (size-1), end =" ")
        else:
            print("* ", end = "  " * (size-1))
    print(end =" " *size )

n =int(input("Enter size of drawing (n>= 3):"))
for i in range(n):
    draw_c(n,i)
    draw_o(n,i)
    draw_d(n,i)
    draw_e(n,i)
    print()
