
def rabbits(month):
    if month == 0 or month ==1:
        return 1
    else:
        return rabbits(month -1) + rabbits(month-2)


for i in range(5):
    print('Month {}: {} pair(s) of rabbit'.format(i, rabbits(i+1)))
