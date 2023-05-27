def bytes_to_kilobytes():
    kilobytes = size
    bytes = kilobytes / 1000
    print(f"Number of kilobytes = {bytes}")

def bytes_to_megabytes():
    megabytes = size
    bytes = megabytes / 1000000
    print(f"Number of megabytes = {bytes}")

def bytes_to_gigabytes():
    gigabytes = size
    bytes = gigabytes / 1000000000
    print(f"Number of gigabytes = {bytes}")
    
def bytes_to_terabytes():
    terabytes = size
    bytes = terabytes / 1000000000000
    print(f"Number of terabytes = {bytes}")

size = float(input('Enter a size in bytes:'))

if 1 <= size <= 999999:
    bytes_to_kilobytes()

if 1000000 <= size <= 999999999:
    bytes_to_megabytes()

if 1000000000 <= size <= 999999999999:
    bytes_to_gigabytes()

if size >= 1000000000000:
    bytes_to_terabytes()