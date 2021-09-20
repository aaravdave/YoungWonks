balance, interest_type, years, rate = [input(f'{i}: ') for i in ['Balance', 'Type of Interest', 'Years', 'Rate']]
balance, interest_type, years, rate = int(balance.strip('$')), interest_type.lower(), int(years), int(rate.strip('%'))

if interest_type == 'simple':
    balance += balance * rate / 100 * years
elif interest_type == 'compound':
    for i in range(years):
        balance += balance * rate / 100
else:
    quit('Unknown Interest Type.')
balance = round(balance, 2)
print(f'\nYour balance in {years} years at a {rate}% rate would be ${balance}.')
