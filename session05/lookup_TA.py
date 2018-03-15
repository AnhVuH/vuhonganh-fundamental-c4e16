teencode = {
    "hc": "Học",
    "ng": "người",
    "pt": "phát triển",
    "eny": "em người yêu",
    "any": "anh người yêu",
    "ngta":" người ta",
    }

while True:

    for key in teencode:
        print(key, end="\t")
        print()
    print('*'*20)

    code = input("your code?")

    if code in teencode:
        print("Code:", code)
        print('Translation: ',teencode[code])
    else:
        print("Not found")
        choice = input('Do you want to contribute this code? (Y/N)').lower()
        if choice == 'y':
            translation = input('Translation? ')
            teencode[code]= translation
            print('Updated')
        else:
            break
