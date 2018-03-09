items = ['T-Shirt', 'Sweater']

def create():
    new = input('Enter new item: ')
    items.append(new)


def read():
    print('Our items: ', end ='')
    print(*items, sep = ', ')
    print()


def update():
    pos = int(input("Update position? "))
    new = input("New item? ")

    if pos > len(items):
        ask = input("We only have {} positions.Do you want to add new item? (y/n) ".format(len(items)))
        if ask == 'y':
            items.append(new)
        else:
            print("Choose another position")
    else:
        items[pos-1] = new

def delete():
    pos = int(input("Delete position? "))
    if pos >len(items):
        print('Can not delete item in position {} !!! We only have {} items.'.format(pos,len(items)))
    else:
        del items[pos-1]

while True:
    request = input('Welcome to our shop, what do you want (C, R, U, D)?')
    if request == 'c' or request =='C':
        create()
        read()
    elif request == 'r' or request == 'R':
        read()
    elif request == 'u' or request == 'U':
        update()
        read()
    elif request == 'd' or request == 'D':
        delete()
        read()
    else:
        print("Do you want to quit? (y/n)")
        if(input() == 'y'):
            break
