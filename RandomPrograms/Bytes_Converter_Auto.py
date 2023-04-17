def bytes_to_kilobytes():
    kilobytes = size
    bytes = kilobytes / 1000
    print('Number of kilobytes = {0}'.format(bytes))

def bytes_to_megabytes():
    megabytes = size
    bytes = megabytes / 1000000
    print('Number of megabytes = {0}'.format(bytes))

def bytes_to_gigabytes():
    gigabytes = size
    bytes = gigabytes / 1000000000
    print('Number of gigabytes = {0}'.format(bytes))

def bytes_to_terabytes():
    terabytes = size
    bytes = terabytes / 1000000000000
    print('Number of terabytes = {0}'.format(bytes))

size = float(input('Enter a size in bytes:'))

if 1 <= size <= 999999:
    bytes_to_kilobytes()

if 1000000 <= size <= 999999999:
    bytes_to_megabytes()

if 1000000000 <= size <= 999999999999:
    bytes_to_gigabytes()

if size >= 1000000000000:
    bytes_to_terabytes()