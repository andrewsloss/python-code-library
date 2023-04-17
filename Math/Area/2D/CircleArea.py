import math

# π * r^2

def CircleArea():
    print('Radius =')
    r = float(input('> '))
    r2 = float(r ** 2)
    area = float(r2 * math.pi)
    print('Area =')
    print('> ',str(r2),'π')
    print('> ',area)

CircleArea()