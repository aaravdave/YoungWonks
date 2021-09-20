def factorial(number):
    if number == 1:
        return number
    return number * factorial(number - 1)

print(factorial(int(input('Enter a number: '))))
