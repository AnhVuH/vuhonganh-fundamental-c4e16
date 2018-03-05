for row in range(1,10):
    for col in range(1,10):
        num = row*col
        print(num, end =" ")
        if num <10:
            print(end =" ")
    print()
