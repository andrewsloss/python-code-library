import math

# (d1 * d2) / 2

def RhombusKiteArea():
    print('Diagonal 1 =')
    d1 = float(input('> '))
    print('Diagonal 2 =')
    d2 = float(input('> '))
    d1d2 = (d1 * d2)
    area = (d1d2 / 2)
    print(area)

RhombusKiteArea()