import random
import time



class race:
    def __init__(self, turtle, rabbit):
        self.turtle = turtle
        self.rabbit = rabbit

    def moveTurtle(self):
        r = random.randrange(9) + 1
        turtleMoves = [3, 6]
        if (r >= 1 and r <= 5):
            self.turtle = turtleMoves[0]
        elif (r == 6 or r == 7):
            self.turtle = -turtleMoves[1]
        else:
            self.turtle = 1
        return self.turtle

    def moveRabbit(self):
        r = random.randrange(9) + 1
        rabbitMoves = [9, 12, 2]
        if (r == 3 or r == 4):
            self.rabbit = rabbitMoves[0]
        elif (r == 5):
            self.rabbit = -rabbitMoves[1]
        elif (r >= 6 and r <= 8):
            self.rabbit = rabbitMoves[2]
        elif (r > 8):
            self.rabbit = -2

        return self.rabbit


