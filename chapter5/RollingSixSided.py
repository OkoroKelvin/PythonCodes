def calculate_product(*args):
    product = 1
    for value in args:
        product *= value
    return product


print(calculate_product(*range(1,6,2)))

