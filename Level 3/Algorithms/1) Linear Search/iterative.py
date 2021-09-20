from random import randint

nums = [randint(1, 100) for _ in range(randint(20, 21))]
num_find = int(input('Enter a number: '))

for ind, num in enumerate(nums):
    if num_find == num:
        print(ind + 1)
        break
else:
    print('Sorry, that was not in the list.')
