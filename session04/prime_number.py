#input
number = int(input("Enter a number: "))

#process
is_not_prime = False

# for i in range(2,number):
#     if number % i == 0:
#         is_not_prime = True
#         break
i = 2
while i <= (number**0.5):  # dung while de tranh khai can ra so le
    if number % i ==0:
        is_not_prime = True
        break
    i += 1

#output
if is_not_prime:
    print(number, "is not a prime number")
else:
    print(number, "is a prime number")
