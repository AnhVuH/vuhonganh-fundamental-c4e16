from random import choice

characters = list("photography")
rand_char = choice(characters)

new = []
while len(new) < len(characters):
    if rand_char not in new or new.count(rand_char) < characters.count(rand_char):
        new.append(rand_char)
    else:
        rand_char = choice(characters)
print(*new)
answer = input("Your answer: ")
if answer == "photography":
    print("Hura")
else:
    print(":(")
