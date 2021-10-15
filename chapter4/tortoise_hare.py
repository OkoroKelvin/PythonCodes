import random

race_course = [""] * 70


def tortoise_move():
    num = random.randint(1, 10)
    if 1 <= num <= 5:
        return 3
    elif 6 <= num <= 7:
        return -6
    else:
        return 1


def hare_move():
    num = random.randint(1, 10)
    if 1 <= num <= 2:
        return 0
    elif 3 <= num <= 4:
        return 9
    elif num == 5:
        return -12
    elif 6 <= num <= 8:
        return 1
    else:
        return -2


def display():
    for index, elem in enumerate(race_course):
        if index % 10 == 0:
            print()
        print(f"{elem:^5}", end="|")

    print()


def clear_screen():
    import os
    os.system("cls")
    # print("\n" * 20)


def delay(seconds):
    import time
    time.sleep(seconds)


print("BANG !!!! \nAND THEY'RE OFF !!!!!")
tortoise, hare = 0, 0
while True:
    race_course[tortoise], race_course[hare] = "", ""
    tortoise += tortoise_move()
    hare += hare_move()
    if tortoise >= 69 and hare >= 69:
        print("It's a tie")
        break
    elif tortoise >= 69:
        print("TORTOISE WINS!!! YAY!!!")
        break
    elif hare >= 69:
        print("Hare wins")
        break

    if tortoise < 0:
        tortoise = 0
    if hare < 0:
        hare = 0
    if tortoise == hare:
        race_course[tortoise] = "OUCH!"
    else:
        race_course[tortoise] = "T"
        race_course[hare] = "H"

    display()
    delay(5)
    clear_screen()
