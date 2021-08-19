import math

terms = int(input("Kindly input the term number: "))
e = 1
for num in range(1, terms):
    e += (1 / math.factorial(num))
print(e)



