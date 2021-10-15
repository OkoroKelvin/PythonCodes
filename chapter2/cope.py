def list_of_integers(values):
    my_even_list = []
    my_new_even_list = []
    my_odd_list = []
    my_new_odd_list = []
    general_list = []

    for val in values:
        if val % 2 == 0:
            my_even_list.append(val)
        my_new_even_list = sorted(my_even_list)
    for val in values:
        if val % 2 != 0:
            my_odd_list.append(val)
        my_new_odd_list = sorted(my_odd_list)
    for val in my_new_odd_list:
        my_new_even_list.append(val)
    return my_new_even_list


numbers = [3, 2, 17, 0, 7, 6, 7383, 99, 3039, 393, 28839, 8222]
print(list_of_integers(numbers))


