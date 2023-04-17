import randomnumber
#import emailValidate
import getEmail

email = str(getEmail.userEmail)
code = str(randomnumber.generateRandom())

with open("Python Code/sendEmail.py") as f:
    exec(f.read())

while True:
    print("Enter Code")
    inputedCode = str(input("> "))

    if inputedCode == code:
        print("Correct")
        break
    else:
        print("Incorrect")

print("program finished")
quit()