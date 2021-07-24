
for col in range(1, 11):
    for row in range(col):
        print("*", end="")
    print()

for col in range(11, 0, -1):
    for row in range(col):
        print("*", end="")
    print()


for col in range(10, 0, -1):
    for row in range(1, 11 - col, 1):
        print(" ", end="")
    for row2 in range(1, col, +1):
        print("*", end="")
    print()


for col in range(1, 11):
    for row in range(1, 11 - col, 1):
        print(" ", end="")
    for row2 in range(1, col, +1):
        print("*", end="")
    print()
