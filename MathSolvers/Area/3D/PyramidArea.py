import math

# LA = 1/2(p * l)
# SA = B + 1/2(p * l)

choice = 0

def Menu():
    print('Press 1 For Lateral Area')
    print('Press 2 For Total Surface Area')
    global choice
    choice = str(input('> '))

Menu()

def PyramidLA():
    print('la')
    Menu()

def PyramidSA():
    print('sa')
    Menu()

while (True):
    if choice == '1':
        PyramidLA()
    elif choice == '2':
        PyramidSA()
    else:
        break