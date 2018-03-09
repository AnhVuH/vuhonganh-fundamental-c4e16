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

playing = True
turn = 0
while playing:
    answer = input("Your answer: ")
    if answer == "photography":
        print("Hura")
        break
    else:
        print(":(")
        turn += 1
    if turn == 7:
        print("You lose")
        playing = False
