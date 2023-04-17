import math

# LA = π * r * l
# SA = 2B + PH

choice = 0

def Menu():
    print('Press 1 For Lateral Area')
    print('Press 2 For Total Surface Area')
    global choice
    choice = str(input('> '))

Menu()

def ConeLA():
    print('la')
    Menu()

def ConeSA():
    print('sa')
    Menu()

while (True):
    if choice == '1':
        ConeLA()
    elif choice == '2':
        ConeSA()
    else:
        break