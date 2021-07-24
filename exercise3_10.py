from decimal import Decimal
r = Decimal('0.07')
p = Decimal('1000.00')

for year in range(1, 31):
    amount = p * (1 + r) ** year
    print(f'Amount for year {year} is {amount:.2f} ', )
