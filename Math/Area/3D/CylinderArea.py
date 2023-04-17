import math

# LA = 2 * π * r * h
# SA = 2 * π * r^2 + 2 * π * r * h

choice = 0

def Menu():
    print('Press 1 For Lateral Area')
    print('Press 2 For Total Surface Area')
    global choice
    choice = str(input('> '))

Menu()

def CylinderLA():
    print('la')
    Menu()

def CylinderSA():
    print('sa')
    Menu()

while (True):
    if choice == '1':
        CylinderLA()
    elif choice == '2':
        CylinderSA()
    else:
        break