def fahrenheit(temperature_in_celsius):
    f = (9 / 5) * temperature_in_celsius + 32
    return f


celsius = float(input("Kindly input your tenmperature between 0-100celsius"))
print(fahrenheit(celsius))
