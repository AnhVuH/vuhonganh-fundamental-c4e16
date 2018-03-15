import string

dictionary = string.ascii_lowercase
alphabet = {}
for char in dictionary:
    alphabet[char] = 0

string = input("Enter a string: ").lower()
for letter in string:
    if letter in alphabet:
        alphabet[letter] = alphabet.get(letter) + 1

for k, v in alphabet.items():
    if v > 0:
        print(k,v, sep ='  ')
