while True:
    number = int(input('Enter a number: '))
    for i in range(2, number):
        if number % i == 0:
            print('That number is composite.\n')
            break
    else:
        print('That number is prime.\n')
