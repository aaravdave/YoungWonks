import random

times, fails = 0, 0
for i in range(100000):
    order = []
    for j in range(5):
        order.append(random.randint(1, 6))
    if order == [1, 2, 3, 4, 5]:
        times += 1
    else:
        fails += 1
print(round(times / fails * 100, 2))
