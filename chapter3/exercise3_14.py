terms_number = int(input('kindly input the terms you want'))
n = 1
i = 2
pie = 0
count = 0

for term in range(terms_number):
    num = (4 / n)
    pie += num * (-1) ** i
    i += 1
    n += 2
    print("{:>3d} Term |  {:>3.2f}".format(term + 1, pie))
    # print(f'The {term + 1} term is {pie}')
    # "{:>3d}       | {:>5d}  | {:5d}".format(num, num ** 2, num ** 3))
