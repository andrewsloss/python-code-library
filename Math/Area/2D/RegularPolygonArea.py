import math

# 1/2(a * p)

def RegularPolygonArea():
    print('Apothem =')
    a = float(input('> '))
    print('Permieter =')
    p = float(input('> '))
    ap = (a * p)
    area = (ap / 2)
    print(area)
    
RegularPolygonArea()