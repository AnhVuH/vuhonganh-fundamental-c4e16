numbers = [1 , 3, 10, -1, -3, 5, 11, -5, 30, -2, 1]

check = 1

while check > 0:
    check = 0
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            temp = numbers[i+1]
            numbers[i+1] = numbers[i]
            numbers[i]= temp
            check +=1
print(numbers)
