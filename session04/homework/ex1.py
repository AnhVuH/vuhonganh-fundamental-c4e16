name = input('Your full name: ').lower()

words = name.split()
for i in range(len(words)):
    words[i] = words[i].capitalize()
    
print('Updated:', ' '.join(words))
