def product(*args):
    products = 1
    for value in args:
        products *= value
    return products


print(product(1, 2, 3, 4, 5, 6))
print(product(1, 2, 3, 3, 7, 8, 7))
