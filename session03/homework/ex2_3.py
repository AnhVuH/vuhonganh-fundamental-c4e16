flock = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is Hong Anh and these are my flock')
print(flock)
print()

max_size = max(flock)
print("Now my biggest sheep has size {} let's shear it".format(max_size))
print()

pos_max = flock.index(max_size)
flock[pos_max] = 8
print('After shearing, here is my flock')
print(flock)
