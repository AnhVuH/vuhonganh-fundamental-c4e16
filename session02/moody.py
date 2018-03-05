from random import randint
mood = randint(0,100)
print(mood)
if mood <= 30:
    print("T_T")
elif mood <= 60:
    print(".-.")
else:
    print("Let's rock & roll")
