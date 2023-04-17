def FizzBuzz():
    for i in range(100):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def loopTest():
    for n in range(1, 11):
        print(n)

def loopTestBy2():
    for n in range(0, 11, 2):
        print(n)

def loopTestBackwards():
    for n in range(10, 0, -1):
        print(n)

loopTestBackwards()