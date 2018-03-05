#d = int(input("Canh:"))
# for i in range(1,7):
#     for j in range(i):
#         print(" * ", end="")
#     print()

# for i in range(1,7):
#     for j in range(7-i):
#         print(" ", end="")
#     for k in range(i):
#         print("*", end ="")
#     print()

# for i in range(6):
#     for j in range(6):
#         if j >= 5 -i:
#             print("*", end="")
#         else:
#             print(" ", end = "")
#         print ()


for i in range(1,7):
    if i ==1  or i == 6:
        print("* "*6, end = "")
    elif i <6:
        for j in range(7-i-1):
            print("  ", end="")
        print("*", end="")
    # else:
    #     print("* "*6, end ="")
    print()
