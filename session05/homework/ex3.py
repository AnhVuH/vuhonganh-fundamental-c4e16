bacterias = int(input('How many B bacterias arer there? '))
minutes = int(input('How much time in minutes will we wait? '))

for time in range(1,minutes,2):
    bacterias *= 2

print("After {} minutes, we would have {} bacterias".format(minutes, bacterias))
