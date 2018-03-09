print("Hi there, here are my fav things so far")
things = ['chup anh', 'ngu', 'dap xe']

for index, item in enumerate(things):
    print(index + 1,'. ', item, sep = "")

pos = int(input("Position you want to update? "))
new_thing = input("Your replacing fav? ")
if pos <= len(things):
    things[pos-1]= new_thing
else:
    things.append(new_thing)

for index, item in enumerate(things):
    print(index + 1,'. ', item, sep = "")
