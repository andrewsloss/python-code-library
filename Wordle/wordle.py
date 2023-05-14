import random

file = open("C:/Users/Andrew/OneDrive/Desktop/six.txt", "r")

words = []

for x in file:
    words.append(x)

def getWord(words):
    num = 0
    num = random.randrange(0, len(words))
    word = words[num]
    print(word)

getWord(words)