import random

times, fails = 0, 0
for i in range(100000):
    total = 0
    for j in range(3):
        total += random.randint(1, 6)
    if total == 5:
        times += 1
    else:
        fails += 1
print(round(times / fails * 100, 2))
