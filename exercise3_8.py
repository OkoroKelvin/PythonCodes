import math

count = 1
total = 0
product = 1
largest = -math.inf
smallest = math.inf

while count <= 4:

    num = int(input(f'Kindly input number{count}'))

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    total += num
    product *= num

    count += 1

average = total / 4
print('The average is:', average)
print('The total: ', total)
print('The largest: ', largest)
print('The smallest: ', smallest)
