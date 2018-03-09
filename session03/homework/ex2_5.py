flock = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is Hong Anh and these are my flock')
print(flock)
print()
for i in range(4):
    print('MONTH {} :'.format(i+1))
    print('One month has passed, now here is my flock')
    for j in range(len(flock)):
        flock[j] += 50
    print(flock)
    max_size = max(flock)
    print("Now my biggest sheep has size {} let's shear it".format(max_size))

    pos_max = flock.index(max_size)
    flock[pos_max] = 8
    print('After shearing, here is my flock')
    print(flock)
    print()
