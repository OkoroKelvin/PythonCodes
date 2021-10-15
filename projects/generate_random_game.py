import random


def guess(x):
    random_number = random.randint(1, x)
    guess_number = 0
    while guess_number != random_number:
        guess_number = int(input(f'Guess a number between 1 and {x}:'))
        if guess_number < random_number:
            print(f'Sorry, guess again. Too low. Guessed number{guess_number} and Random_number:{random_number}')
        elif guess_number > random_number:
            print(f'Sorry, guess again. Too high.Guessed number{guess_number} and Random_number:{random_number}')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!!')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess_number = random.randint(low, high)
        feedback = input(f'is {guess_number}too high (H), too low (L), or correct (C)??').lower()
        if feedback == 'h':
            high = guess_number - 1
        elif feedback == 'l':
            low = guess_number + 1

        print(f'Yay! The computer guessed your number, {guess_number}, correctly')


guess(10)
