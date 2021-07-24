factorial_number = int(input('Kindly input the factorial number: '))
new_factorial_number = 1
count = 0
while factorial_number != 0:
    new_factorial_number *= factorial_number
    factorial_number -= 1
    count += 1

print(f'The factorial of {count} is {new_factorial_number}')
