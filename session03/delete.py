print("Hi there, here are my fav things so far")
things = ['chup anh', 'ngu', 'dap xe']

for index, item in enumerate(things):
    print(index+1, '. ', item, sep ='')

# pos = int(input("position want to delete:"))
# del things[pos-1]
# things.pop(pos-1)

name = input("name:")

if name in things:
    things.remove(name)
else:
    print("Not found")

for index, item in enumerate(things):
    print(index+1, '. ', item, sep ='')
