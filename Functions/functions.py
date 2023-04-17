def isEven(num):
    if num & 2 == 0:
        return True
    else:
        return False

def isOdd(num):
    if num & 2 == 1:
        return True
    else:
        return False
    
def length(object):
    count = 0
    for x in object:
        count += 1
    return count

def average(array):
    total = 0
    count = 0
    for x in array:
        total += x
        count += 1
    average = total / count
    return average