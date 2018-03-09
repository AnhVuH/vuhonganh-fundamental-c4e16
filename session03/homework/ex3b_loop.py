from random import choice, randint
words = ["champion", "hexagon", "meticulous","photography"]

picked_word = words[randint(0,len(words)-1)]

characters = list(picked_word)
rand_char = choice(characters)
new = []

while len(new) < len(characters):
    if rand_char not in new or new.count(rand_char) < characters.count(rand_char):
        new.append(rand_char)
    else:
        rand_char = choice(characters)

playing = True
turn = 0
while playing:
    print(*new)
    answer = input('Your answer: ')
    if answer == picked_word:
        print('Hura')
        break
    else:
        print(':(')
        turn += 1
    if turn == 7:
        print("You lose")
        playing = False
