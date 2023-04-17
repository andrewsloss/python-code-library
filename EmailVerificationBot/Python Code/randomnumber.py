import random

def generateRandom():
    randomList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    List = []
    num = ""

    for x in range(0, 6):
        randomNum = random.choice(randomList)
        List.append(randomNum)


    for y in List:
        num += (str(y))
    
    return num