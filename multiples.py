number_1 = 1024
number_2 = 10
new_number_1 = number_1 % 4
new_number_2 = number_2 % 2

if new_number_1 == 0:
    print(number_1, "is a multiple of 4")
else:
    print(number_1, "is not a multiple of 4")

if number_2 == 0:
    print(number_2, "is a multiple of 2")
else:
    print(number_2, "is not a multiple of 2")