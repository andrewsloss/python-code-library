import math

# 1/2(b1 + b2) * h

def TrapezoidArea():
    print('Base 1 =')
    b1 = float(input('> '))
    print('Base 2 =')
    b2 = float(input('> '))
    print('Height =')
    h = float(input('> '))
    sum1 = (b1 + b2)
    sum2 = (sum1 / 2)
    area = (sum2 * h)
    print(area)

TrapezoidArea()