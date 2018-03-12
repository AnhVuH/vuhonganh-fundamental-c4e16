# array = input('Enter a sequence of number, separated by space:')
# list_num = array.split()
#
# #print (list_num)
# int_list = []
# for item in list_num:
#     int_list.append(int(item))
#
# #print(int_list)
# sort = True
# for i in range(len(int_list)-1):
#     if int_list [i] > int_list[i+1]:
#         sort = False
#         break
# if sort:
#     print('Your sequence is already sorted')
# else:
#     print('Your sequence is not sorted yet')

from sort_numbers import sort_num

s = input('Enter a sequence of numbers, separated by space: ')

words = s.strip().split(' ')

numbers = []
for word in words:
    numbers.append(int(word))

is_sorted = True
for i in range(len(numbers)-1):
    if numbers[i] > numbers[i+1]:
        is_sorted = False
        break
if is_sorted:
    print('Your sequence is already sorted')
else:
    print('Your sequence is not sorted yet')

sort_num(numbers)
