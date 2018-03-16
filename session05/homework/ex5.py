prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
    }
stock = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 32,
    "pear" : 15
    }

for fruit in prices:
    print(fruit)
    print('price: ', prices[fruit])
    print('stock: ', stock[fruit])
    print()

total = 0
for fruit in prices:
    total += prices[fruit] * stock[fruit]

print('You make: ', total)
