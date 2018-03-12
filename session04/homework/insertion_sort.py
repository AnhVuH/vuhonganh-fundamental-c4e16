numbers = [1 , 3, 10, -1, -3, 5, 11, -5, 30, -2, 1]

for i in range(len(numbers)):
    insert_num = numbers[i]
    j = i
    while j > 0 and insert_num < numbers[j-1]:
        numbers[j] = numbers[j-1]
        j -=1
    numbers[j] = insert_num

print(numbers)
