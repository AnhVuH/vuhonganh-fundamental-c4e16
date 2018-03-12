balance = input('Enter your balance:').strip().lstrip('0')
numbers = list(balance)

for i in range(len(numbers)-3, 0, -3):
    numbers.insert(i, ',')

print('Your updated balance: $',''.join(numbers), sep='')
