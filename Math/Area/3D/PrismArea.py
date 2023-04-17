import math

# LA = PH
# SA = 2B + PH

choice = 0

def Menu():
    print('Press 1 For Lateral Area')
    print('Press 2 For Total Surface Area')
    global choice
    choice = str(input('> '))

Menu()

def PrismLA():
    print('la')
    Menu()

def PrismSA():
    print('sa')
    Menu()

while (True):
    if choice == '1':
        PrismLA()
    elif choice == '2':
        PrismSA()
    else:
        break