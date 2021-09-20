variables = {}
while (equation := None) != 'QUIT':
    equation, num, op = [int(i) if i.isnumeric() else i for i in input('> ').split()], None, None
    for i in equation:
        if str(i) in '+-*/=':
            op = i
        elif i == '':
            continue
        else:
            if num is None:
                num = i
            else:
                if type(num) == str and op != '=':
                    num = variables[num]
                if type(i) == str and op != '=':
                    i = variables[i]
                if op == '+':
                    num += i
                elif op == '-':
                    num -= i
                elif op == '*':
                    num *= i
                elif op == '/':
                    num /= i
                elif op == '=':
                    variables[num] = i
                    break
                else:
                    print('Invalid Operation\n')
                    break
    else:
        if str(num).endswith('.0'):
            num = int(num)
        print(str(num) + '\n')
print('Successfully Quit')
