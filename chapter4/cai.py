import random


def generate_numbers():
    return random.randint(1, 10), random.randint(1, 9)


def display_question():
    num1, num2 = generate_numbers()
    answer = num1 * num2
    return f"How much is {num1} times {num2}", answer


def cai():
    question, answer = display_question()

    while True:
        print(question)
        response = int(input("your answer: "))
        if response == answer:
            print("Very good")
            question, answer = display_question()
        else:
            print("No. Please try again.")


cai()

