import math

# 1/2(b * h)

def TriangleArea():
    print('Base =')
    b = float(input('> '))
    print('Height =')
    h = float(input('> '))
    bh = (b * h)
    area = (bh / 2)
    print(area)

TriangleArea()