from math import sqrt
for a in range(1, 101):
    for b in range(1, 101):
        c = sqrt(a ** 2 + b ** 2)
        if c == int(c):
            print(f'{a}² + {b}² = {int(c)}²')
