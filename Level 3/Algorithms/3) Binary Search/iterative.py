from random import randint

nums = sorted([randint(1, 100) for _ in range(randint(20, 21))])
print(nums)
num_find = int(input('Enter a number: '))

ind = len(nums) // 2

print(nums.index(num_find))
while True:
    print(f'{ind} is the index, and the number is {nums[ind]}')
    if num_find == nums[ind]:
        print(ind + 1)
        break
    elif num_find > nums[ind]:
        ind = (ind + len(nums)) // 2
    else:
        ind = ind // 2
