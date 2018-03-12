numbers = [1 , 3, 10, -1, -3, 5, 11, -5, 30, -2, 1]

for i in range(len(numbers)-1):
    min_pos = i
    for j in range(i+1,len(numbers)):
        if numbers[j] < numbers[min_pos]:
            min_pos = j
    if min_pos != i:
        temp = numbers[min_pos]
        numbers[min_pos] = numbers[i]
        numbers[i] = temp

print(numbers)
