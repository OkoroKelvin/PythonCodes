total_miles_per_gallon = 0
count = 0
gallon_used = float(input('Enter the gallons used (-1 to end):'))

while gallon_used != -1:
    miles_driven = int(input('Enter the miles driven :'))
    miles_per_gallon = miles_driven / gallon_used
    total_miles_per_gallon += miles_per_gallon
    print(f'The miles/gallons for this tank was {miles_per_gallon}')
    count += 1
    gallon_used = float(input('Enter the gallons used (-1 to end):'))


average_total_miles_per_gallon = total_miles_per_gallon / count
print(f'The overall average miles/gallon was {average_total_miles_per_gallon}')

