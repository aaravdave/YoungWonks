from math import sqrt
a, b = list(map(int, [input(f'{i}: ') for i in ['a', 'b']]))
c = a ** 2 + b ** 2
print(f'The length of \'c\' would be {sqrt(c)} or √{c}.')
