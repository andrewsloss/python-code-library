count = 0

class LogIn:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def PrintInfo(self):
        print(self.username, self.password)

print('Create Your Account')
account = LogIn(str(input('Username > ')), str(input('Password > ')))
print('Account Created!')
print('Log In To Your New Account')
username = str(input('Username > '))
password = str(input('Password > '))
if username == account.username:
    count = count + 1
else:
    count = count
if password == account.password:
    count = count + 1
else:
    count = count
if count == 2:
    print('Log In Success')
else:
    print('Log In Fail')    