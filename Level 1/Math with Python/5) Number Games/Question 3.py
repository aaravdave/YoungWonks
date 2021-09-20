def factors(num):
    nums = [1, num]
    for item in range(2, num):
        if num % item == 0:
            nums.insert(-1, item)
    return nums

while True:
    number = int(input('Enter a number: '))
    current, numbers = 2, []
    while number != 1:
        if number % current == 0:
            number //= current
            numbers.append(current)
        else:
            current += 1
            while True:
                if factors(current) != 2:
                    break
                current += 1
    print(f'{numbers}\b\n'[1:])
