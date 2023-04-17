import math
import random

# =========================================================================================================================================================================================================

# Python Calculator
def Menu():
    print('Press 1 For Quadratic Equation Solver')
    print('Press 2 For Pythagorean Theorem Solver')
    print('Press 3 For PI')
    print('Press 4 For Polygon Side Length Calculator')
    global choice
    choice = str(input('> '))


Menu()

# =========================================================================================================================================================================================================

# Quadratic Equation Solver
def QuadraticCalculator():
    print('Enter your a value')
    a = float(input('> '))
    print('Enter your b value')
    b = float(input('> '))
    print('Enter your c value')
    c = float(input('> '))
    sum1 = (b * -1)
    sum2 = (((b ** 2) - (4 * a * c)) ** (1 / 2))
    sum3_1 = (sum1 + sum2)
    sum3_2 = (sum1 - sum2)
    sum4_1 = (sum3_1 / (2 * a))
    sum4_2 = (sum3_2 / (2 * a))
    print('x = ', sum4_1)
    print('x = ', sum4_2)
    print('\n')
    Menu()


# =========================================================================================================================================================================================================

# Pythagorean Theorem
def PythagoreanTheorem():
    print('Enter your a value')
    a = float(input('> '))
    print('Enter your b value')
    b = float(input('> '))
    sum1 = ((a ** 2) + (b ** 2))
    sum2 = (sum1 ** (1 / 2))
    print('c = ', sum2)
    print('c = ', sum2 ** (2))
    print('\n')
    Menu()

# =========================================================================================================================================================================================================

# PI
def PI():
    print(math.pi)
    print('\n')
    Menu()

# =========================================================================================================================================================================================================\

# Polygon Side Length Calculator
def PolygonLength():
    print('Enter a number of sides between 2-8')
    sides = str(input('> '))
    if sides == '2':
        S2()
    elif sides == '3':
        pass
    elif sides == '4':
        pass
    elif sides == '5':
        pass
    elif sides == '6':
        pass
    elif sides == '7':
        pass
    elif sides == '8':
        pass
    else:
        print('ERROR')

def S2():
    X1 = str(input('X1 = '))
    Y1 = str(input('Y1 = '))
    X2 = str(input('X2 = '))
    Y2 = str(input('Y2 = '))
    if X1[0] == '-':
        float(X1)
        X1 = (X1 * -1)
    else:
        float(X1)
    if Y1[0] == '-':
        float(Y1)
        Y1 = (Y1 * -1)
    else:
        float(Y1)
    if X2[0] == '-':
        float(X2)
        X2 = (X2 * -1)
    else:
        float(X2)
    if Y2[0] == '-':
        float(Y2)
        Y2 = (Y2 * -1)
    else:
        float(Y2)
    print(X1 + 'a', Y1 + 'b', X2 + 'c', Y1 + 'd')

# =========================================================================================================================================================================================================

while (True):
    if choice == '1':
        QuadraticCalculator()
    elif choice == '2':
        PythagoreanTheorem()
    elif choice == '3':
        PI()
    elif choice == '4':
        PolygonLength()
    elif choice == '5':
        pass
    else:
        break