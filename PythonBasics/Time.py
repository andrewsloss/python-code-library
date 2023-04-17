import time
import datetime

def delayTime():
  def timeTest():
    x = datetime.datetime.now()
    for a in range(10000000):
        a += 1
    y = datetime.datetime.now()
    for b in range(10000000):
        b += 1
    z = datetime.datetime.now()
    for c in range(10000000):
        c += 1
    print(str(x))
    print(str(y))
    print(str(z))
    print("")
  for i in range(6):
    timeTest()

def sleepTime():
  time1 = datetime.datetime.now()
  print(time1)
  print("5")
  time.sleep(1)
  print("4")
  time.sleep(1)
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  time.sleep(1)
  time2 = datetime.datetime.now()
  print(time2)

def stopwatch():
  print("1. Seconds")
  print("2. Minutes")
  print("3. Hours")
  format = input("> ")
  print("\nEnter time.")
  if format == "1":
    stopwatchTime = float(input("> "))
  elif format == "2":
    stopwatchTime = float(input("> ")) * 60
  elif format == "3":
    stopwatchTime = float(input("> ")) * 60 ** 2
  print("")
  while (stopwatchTime > 0):
    print(stopwatchTime)
    stopwatchTime -= 1
    time.sleep(1)
  beeb()

def beeb():
  print("BEEB, ", end = "")
  time.sleep(1)
  print("BEEB, ", end = "")
  time.sleep(1)
  print("BEEB, ", end = "")
  time.sleep(1)
  print("BEEB, ", end = "")
  time.sleep(1)
  print("BEEB, ", end = "")
  time.sleep(1)
  print("BEEB")


def menu():
  print("1. Delay Time")
  print("2. Sleep Time")
  print("3. Stopwatch")
  choice = input(str("> "))
  if choice == "1":
    print("")
    delayTime()
  elif choice == "2":
    print("")
    sleepTime()
  elif choice == "3":
    print("")
    stopwatch()
  else:
    print("\nI Quit, Bye!")
    quit()

menu()