KEL = ["O", "X", "O", "Y", "O", "X", "Z", "X", "J", "L", "P", "U"]

for i in range(0, 11, 3):
    for j in range(i, i + 3):
        print("|", KEL[j], end=" ")
    print()
