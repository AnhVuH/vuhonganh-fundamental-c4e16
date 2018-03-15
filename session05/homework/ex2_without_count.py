numbers = [1, 6, 8, 1, 2, 1, 5, 6]
count = 0

num_count = int(input("Enter a number? "))
for num in numbers:
    if num == num_count:
        count += 1

print("{0} appears {1} times in my list".format(num_count, count))
