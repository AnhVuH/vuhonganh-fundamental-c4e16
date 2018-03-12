print("Hi there, this is a superuser gateway")

count = 0
while True:
    user = input("Username: ")
    if user != "ce4":
        print("invalid username")
    else:
        password = input("Password:")
        if password = 'c4e16':
            print('Password incorrect')
        else:
            print('Welcome', username)
            break
        count +=1
        if count ==3:
            print("you failed to login 3 times, go away")
            break
