def loopingArray2D():
    array = [[1,2,3], [4,5,6], [7,8,9]]
    for x in range(0, len(array), 1):
        for y in range(0, len(array[0]), 1):
            print(array[x][y], end = " ")
    print()

def multiplyArray2D():
    array = [[1,2,3], [4,5,6], [7,8,9]]
    for x in range(0, len(array), 1):
        for y in range(0, len(array[0]), 1):
            if x < 2 and y < 2:
                array[x][y] *= array[x][y+1]
            elif (x == 0 or x == 1) and y == 2:
                array[x][y] *= array[x+1][0]
            elif x == 2 and y < 2:
                array[x][y] *= array[x][y+1]
            else:
                array[x][y] *= 10
    for x in range(0, len(array), 1):
        for y in range(0, len(array[0]), 1):
            print(array[x][y], end = " ")
    print()

def multiplyArray2D_2():
    array = [[1,2,3], [4,5,6], [7,8,9]]
    for x in range(0, len(array), 1):
        for y in range(0, len(array[0]), 1):
            if x < len(array) and y < len(array) or x == len(array) and y < len(array):
                array[x][y] *= array[x][y+1]
            elif (x == 0 or x == 1) and y == 2:
                array[x][y] *= array[x+1][0]
            else:
                array[x][y] *= 10
    for x in range(0, len(array), 1):
        for y in range(0, len(array[0]), 1):
            print(array[x][y], end = " ")
    print()

multiplyArray2D()