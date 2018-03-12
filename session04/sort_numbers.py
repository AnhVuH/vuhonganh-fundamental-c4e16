#numbers = [1 , 3, 10, -1, -3, 5, 11, -5, 30]
def sort_num(numbers):
    sorted_list =[]

    while True:
        min_numb = min(numbers)

        sorted_list.append(min_numb)

        numbers.remove(min_numb)

        if len(numbers)==0:
            break

    print(*sorted_list)
