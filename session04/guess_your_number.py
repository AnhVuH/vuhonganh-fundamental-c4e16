
print('Guess your number game')

input("Now think of a number from 0 to 100, then press 'Enter'")
print("""
        All you have to do is to answer to my guess
        'c' if my guess is 'C'orrect
        'l' if my guess is 'L'arger than your number
        's' if y guess is 'S'maller than your number
        """)

low = 0
high = 101
#mid = 50

# answer = input('Is {0} your number ?:'.format(mid))
#
# while answer != 'c':
#     if answer == 's':
#         low = mid
#         mid = (high- low)//2 + low
#     elif answer == 'l':
#         high = mid
#         mid = (high - low)//2 +low
#     answer = input('Is {0} your number ?:'.format(mid))
# print('I knew it')
while True:
    mid = (low + high)//2
    ans = input('Is {0} your number? '.format(mid)).lower()
    if ans == 'c':
        print('I knew it!!!')
        break
    elif ans == 'l':
        high = mid
    elif ans == 's':
        low = mid
    else:
        print('.....')
