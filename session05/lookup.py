words = {"hc": "Học", "ng": "người", "pt": "phát triển", "eny": "em người yêu", "any": "anh người yêu", "ngta":" người ta"}
print(words)
print("*"*10)
loop = True
while loop == True:
    code =input("your coude? ")
    if code in words:
        print(words[code])
        cont = input("Do you want to continue? (Y/N)").lower()
        if cont == 'n':
            break

    else:
        request=input("Not found. Do you want to contribute this word? (Y/N)").lower()
        if request == 'y':
            word =input("enter your translation:")
            words[code]= word
            print("updated")
            cont = input("Do you want to continue? (Y/N)").lower()
            if cont == 'n':
                break
            elif cont == 'y':
                continue
        else:
            loop = False
print (words)
