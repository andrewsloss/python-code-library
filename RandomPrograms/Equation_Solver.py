equation = (input('> '))

l1 = (str(equation[0]))
l2 = (str(equation[1]))
l3 = (str(equation[2]))
l4 = (str(equation[3]))
l5 = (str(equation[4]))
l6 = (str(equation[5]))
l7 = (str(equation[6]))
l8 = (str(equation[7]))
l9 = (str(equation[8]))
l10 = (str(equation[9]))

if l3 == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
    print('3')
elif l2 == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
    print('2')
elif l1 == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
    print('1')
else:
    print('fail')

def print_parts():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l8)
    print(l9)
    print(l10)

# DOES NOT WORK AT ALL