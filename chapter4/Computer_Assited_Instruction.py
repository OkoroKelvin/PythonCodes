import random


def random_value_function():
    number1 = random.randrange(1, 10)
    number2 = random.randrange(1, 10)
    return number1, number2


def display_result(number):
    number1, number2 = number
    print(f'How much is {number1} times {number2} ?')


def calculate_value(number_calculate):
    number_calculate1, number_calculate2 = number_calculate
    return number_calculate1 * number_calculate2


tuple_random_value = random_value_function()
display_result(tuple_random_value)
print('Kindly input your answer')
answer = int(input())

if calculate_value(tuple_random_value) == answer:
    (print(end=""))
else:
    (print(end=""))

while True:
    tuple_random_value = random_value_function()
    display_result(tuple_random_value)
    print('Kindly input your answer')
    answer = int(input())
    if calculate_value(tuple_random_value) == answer:
        (print("Very good"))
    else:
        (print("No. Please try again."))


