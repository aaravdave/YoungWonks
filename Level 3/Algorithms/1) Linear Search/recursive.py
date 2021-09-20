from random import randint


def find(number, numbers, index):
    if index == len(nums):
        return 'Sorry, that was not in the list.'
    if numbers[index] == number:
        return index + 1
    return find(number, numbers, index + 1)


nums = [randint(1, 100) for _ in range(randint(20, 21))]
num_find = int(input('Enter a number: '))
print(find(num_find, nums, 0))
