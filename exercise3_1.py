passes = 0
failures = 0
result = int(input('Enter result for student (1 is for pass, 2 is for fail, -1 to see results) : '))
while result != -1:
    if result == 1:
        passes = passes + 1
    elif result == 2:
        failures = failures + 1
    else:
        print("Kindly type in scores between 1 and 2")
    result = int(input('Enter result for student (1 is for pass, 2 is for fail, -1 to see results) : '))

print('Passed:', passes)
print('Failed: ', failures)

if passes > 8:
    print('Bonus to instructor')
