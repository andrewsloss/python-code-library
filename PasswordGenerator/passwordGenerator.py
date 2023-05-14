import random

def length(object):
    count = 0
    for x in object:
        count += 1
    return count

password = ""
passwordLength = 0

upperCase = False
lowerCase = False
numbers = False
symbols = False

array = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", "0123456789", "!@#$%^&*()"]
string = ""
randomChar = 0

def getParameters():
    global passwordLength, upperCase, lowerCase, numbers, symbols

    passwordLength = int(input("Password Length: "))
    upperCaseChoice = str(input("Use Upper Case Letters? (Y/N): "))
    if upperCaseChoice == "Y":
        upperCase = True
    lowerCaseChoice = str(input("Use Lower Case Letters? (Y/N): "))
    if lowerCaseChoice == "Y":
        lowerCase = True
    numbersChoice = str(input("Use Numbers? (Y/N): "))
    if numbersChoice == "Y":
        numbers = True
    symblosChoice = str(input("Use Symbols? (Y/N): "))
    if symblosChoice == "Y":
        symbols = True

getParameters()

if upperCase == True:
    string += array[0]
if lowerCase == True:
    string += array[1]
if numbers == True:
    string += array[2]
if symbols == True:
    string += array[3]

for x in range(passwordLength):
    randomChar = random.randint(0, length(string))
    password += string[randomChar - 1]

print("Password =", password)
print("Password Length = ", length(password))
