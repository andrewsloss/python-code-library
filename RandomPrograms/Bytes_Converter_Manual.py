def print_menu():
    print('1. Bytes to kilobyte')
    print('2. Bytes to megabyte')
    print('3. Bytes to gigabyte')
    print('4. Bytes to terabyte')

def bytes_to_kilobyte():
    kilobyte = float(input('Enter a size in bytes: '))
    bytes = kilobyte / 1000
    print('Number of kilobyte = {0}'.format(bytes))

def bytes_to_megabyte():
    megabyte = float(input('Enter a size in bytes: '))
    bytes = megabyte / 1000000
    print('Number of megabyte = {0}'.format(bytes))

def bytes_to_gigabyte():
    gigabyte = float(input('Enter a size in bytes: '))
    bytes = gigabyte / 1000000000
    print('Number of gigabyte = {0}'.format(bytes))

def bytes_to_terabyte():
    terabyte = float(input('Enter a size in bytes: '))
    bytes = terabyte / 1000000000000
    print('Number of terabyte = {0}'.format(bytes))

print_menu()

choice = input('Which conversion would you like to do?: ')

if choice == '1':
    bytes_to_kilobyte()

if choice == '2':
    bytes_to_megabyte()

if choice == '3':
    bytes_to_gigabyte()

if choice == '4':
    bytes_to_terabyte()