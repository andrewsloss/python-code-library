import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

passwordLength = int(input("Enter password length: "))

random.shuffle(characters)

password_arr = []

for num in range(passwordLength):
    password_arr.append(characters[num - 1])

password = "".join(password_arr)

print(password)