from math import pi
question = input('Do you want to find the area of a circle, trapezoid, or rectangle: ').lower()
if question == 'circle':
    print(f'\n{pi * (int(input("Radius: ")) ** 2)}')
elif question == 'trapezoid':
    print(f'\n{(int(input("Top Length: ")) + int(input("Bottom Length: "))) / 2 * int(input("Height: "))}')
elif question == 'rectangle':
    print(f'\n{int(input("Length: ")) * int(input("Width: "))}')
else:
    quit('Unidentified Shape.')
