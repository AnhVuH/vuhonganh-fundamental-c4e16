from random import randint

my_num = randint(0,100)
print(my_num)
guess_num = int(input("Guess my number (1-100)? "))
count = 0

while guess_num != my_num or count < 7:
    if guess_num > my_num:
        print("too large")
        guess_num = int(input("Guess my number (1-100)? "))
        count+=1
    elif guess_num < my_num:
        print ("too small")
        guess_num = int(input("Guess my number (1-100)? "))
        count +=1
if count == 7:
    print("you lose")
else:
    print("bingo")
