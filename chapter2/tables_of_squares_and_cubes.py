print("Table of Square and Cube")
print("")
print("{:10s}|  {:4s}|   {:<4s}".format("numbers", "square", "cube"))
print("-"*28)

for num in range(6):
    print("{:>3d}       | {:>5d}  | {:5d}".format(num, num ** 2, num ** 3))
