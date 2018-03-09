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

print(*new)
ans = input('Your answer: ')
if ans == picked_word:
    print('Hura')
else:
    print(':(')
