from math import sqrt
x, y, a, b = list(map(int, input('Enter \'x, y, a, b\': ').split(', ')))
print(round(sqrt(((x - a) ** 2) + ((y - b) ** 2)), 2))
