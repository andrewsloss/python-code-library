count = 0
choice = 0
account = None

class Credentials:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def PrintInfo(self):
        print(self.username, self.password)

def create_account():
    print('\nCreate Your Account')
    global account
    account = Credentials(str(input('Username > ')), str(input('Password > ')))
    print('\nAccount Created!\n')
    Menu()

def login():
    print('\nLog In To Your New Account')
    username = str(input('Username > '))
    password = str(input('Password > '))
    global account
    try:
        if username == account.username:
            global count
            count = count + 1
        if password == account.password:
            count = count + 1
    except:
        print("\nNo Accounts Exist\n")
        count = 3
    if count == 2:
        print('\nLog In Success\n')
    elif count == 3:
        pass
    else:
        print('\nLog In Fail\n')
    count = 0
    Menu()

def Menu():
    print('Press 1 for Log In')
    print('Press 2 for Sign Up')
    global choice
    choice = str(input('> '))

Menu()

while(True):
    if choice == '1':
        login()
    elif choice == '2':
        create_account()
    else:
        break