# num = input("Enter a number:")
# print(len(num))

num = int(input("Enter a number: "))    #input

# count = 0
#if num = 0:
#    count = 1
#else:
    # while num != 0:       # num = 0 -> digit = 0
    #     num = num//10
    #     count += 1
# print(count)

#process
count = 0
while True:
    num = num//10
    count +=1
    if num==0:
        break
#output
print(count)
