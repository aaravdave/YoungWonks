tip, tax, cost = [input(f'{i}: ') for i in ['Tip Percentage', 'Tax Percentage', 'Cost']]
tip, tax, cost = list(map(int, [tip.strip('%'), tax.strip('%'), cost.strip('$')]))

print(f'\nThe total with a %{tip} tip rate and %{tax} tax rate would be ${round(cost + cost * tip / 100 + cost * tax / 100, 2)}.')
