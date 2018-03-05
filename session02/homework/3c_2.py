n = int(input("Enter a number: "))
for row in range(1,n+1):
    for col in range(1,n+1 ):
        num = row *col
        print(num, end = " ")
        length = len(str(n*n)) - len(str(num))
        if length > 0:
            print(" " * length, end="" )
    print()
