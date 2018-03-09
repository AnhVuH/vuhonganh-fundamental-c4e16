flock = [5, 7, 300, 90, 24, 50, 75]

def shearing(month,last_month):
    if month == 0:
        print("Hello, my name is Hong Anh and here is my flock")
        print(flock)
        print()
    else:
        print("MONTH {} :".format(month))
        print('One month has passed, now here is my flock')
        for i in range(len(flock)):
            flock[i] += 50
        print(flock)

    if month < last_month:
        max_size = max(flock)
        print("Now my biggest sheep has size {} let's shear it".format(max_size))

        pos_max = flock.index(max_size)
        flock[pos_max] = 8
        print("After shearing, here is my flock")
        print(flock)
        print()
    else:
        print()

for i in range(4):
    shearing(i,3)

total = 0
for size in flock:
    total += size

print("My flock has size in total:", total)
print ('I would get {} * 2$ = {}$'.format(total, total*2))
