from random import randint

number = 71

playing = True
count = 0

while playing:
    guess = int(input("Your guess? "))

    if guess >number:
        print("too large")
    elif guess < number:
        print("too small")
    else:
        print("bingo")
        break

    count +=1
    if count ==7:
         print("You lose :()")
         break
