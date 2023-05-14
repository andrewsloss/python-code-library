import random

def run():
    score = 0
    complete = False
    anwser = []
    toRender = []
    string = getString()
    for num in range(0, len(string)):
        anwser.append(string[num])
        toRender.append("_")
    render(toRender)
    while (complete == False):
        getGuess(anwser, toRender)
        render(toRender)
        score += 1
        complete = isComplete(toRender)
    print("\n\nGood Job! You finished the puzzle in " + str(score) + " moves.")

def randomNumber():
    return random.randrange(1, 101)

def randomSum(rand):
    array = []
    for x in range (0, rand + 1):
        for y in range (0, rand + 1):
            if (x + y == rand):
                array.append(x)
    return array[random.choice(array)]

def getString():
    random = randomNumber()
    sumOne = randomSum(random)
    sumTwo = random - sumOne
    return str(sumOne) + "+" + str(sumTwo) + "=" + str(random)

def getGuess(anwser, toRender):
    guess = str(input("\n> "))
    print("")
    for num in range(0, len(anwser)):
        if (anwser[num] == guess):
            toRender[num] = guess

def render(toRender):
    for part in (toRender):
        print(part, end = "")

def isComplete(toRender):
    for part in (toRender):
        if (part == "_"):
            return False
    return True

run()
