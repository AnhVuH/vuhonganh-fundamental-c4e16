print("Hi there, here are my fav things so far")
things = ['chup anh', 'ngu', 'dap xe']
print(*things, sep = ', ')
new = input("Name one thing you want to add? ")
things.append(new)

print(*things, sep = ', ')
