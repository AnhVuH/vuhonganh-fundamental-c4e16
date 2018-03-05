num = int(input("Enter the total number of 1's and 0's: "))
for i in range(num):
    if i % 2 ==0:
        print(1, end ="  ")
    else:
        print(0, end ="  ")
