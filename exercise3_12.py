digits = int(input('Kindly input numbers to know if palindrome or not palindrome'))
digit_1 = digits // 10000
digit_2 = (digits // 1000) % 10
digit_3 = (digits // 100) % 10
digit_4 = (digits % 100) // 10
digit_5 = digits % 10

if str(digits) == (str(digit_5) + str(digit_4) + str(digit_3) + str(digit_2) + str(digit_1)):
    print('This is a palindrome figure')
else:
    print('This is not a palindrome figure')
