from options import words
import random

def getWord(words):
    num = random.randrange(0, len(words))
    return words[num]

word = getWord(words)
print(word)