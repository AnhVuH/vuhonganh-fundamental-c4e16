import getpass

name = input("Username: ")
#pass_w = input("Password: ")
pass_w =getpass.getpass("Password")

if name != "C4E":
    print("invalid username")
elif pass_w != "123456":
    print ("wrong password")
else:
    print("welcome", name)
