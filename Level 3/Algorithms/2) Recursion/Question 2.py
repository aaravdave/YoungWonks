def fibonacci(times, previous=0, current=1, string='', current_iter=1):
    if times == current_iter:
        return string
    string += str(current + previous) + ' '
    return fibonacci(times, current, current + previous, string, current_iter + 1)

print(fibonacci(int(input('Enter a number: '))))
