while True:
    number = int(input('Enter a number: '))
    numbers = [1, number]
    for i in range(2, number):
        if number % i == 0:
            numbers.insert(-1, i)
    print(f'{numbers}\b\n'[1:])
