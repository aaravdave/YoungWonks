import random

times, fails = 0, 0
for i in range(100000):
    text = ''
    for j in range(3):
        text += 'abcdefghijklmnopqrstuvwxyz'[random.randint(1, 26) - 1]
    if text == 'cat':
        times += 1
    else:
        fails += 1
print(round(times / fails * 100, 2))
