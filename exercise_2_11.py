number = int(input('Input numbers'))
num1 = number // 10000
num2 = (number // 1000) % 10
num3 = (number // 100) % 10
num4 = (number % 100) // 10
num5 = number % 10

print(str(num1)+"   "+str(num2)+"   "+str(num3)+"   "+str(num4)+"   "+str(num5))


