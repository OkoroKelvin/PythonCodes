x = float(input("Input the X value"))
y = float(input("Input the Y value"))

if x == 0 and y == 0:
    print("It's the origin")

elif (x == 0 and y > 0) or (y == 0 and x > 0):
    print("One of the coordinates is equal to zero")

elif x > 0 and y > 0:
    print("I")

elif x < 0 and y < 0:
    print("III")

elif x > 0 and y < 0:
    print("IV")

elif x < 0 and y > 0:
    print("II")
