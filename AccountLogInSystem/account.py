class User:
    def __init__(self, u, p):
        self.username = u
        self.password = p

class AccountManager:
    def __init__(self):
        self.users = {}

    def signUp(self):
        username = input("\nUsername: ")
        password = input("Password: ")
        if username in self.users:
            print("\nUsername taken!")
            account_manager.signUp()
        else:
            self.users[username] = User(username, password)
            print("\nAccount created!\n")

    def logIn(self):
        username = input("\nUsername: ")
        password = input("Password: ")
        if username in self.users and self.users[username].password == password:
            print("\nLog in success!\n")
        else:
            print("\nLog in fail!\n")

account_manager = AccountManager()

print("--- AccountManager ---\n")

while True:
    print("1. Sign Up")
    print("2. Log In")
    choice = input("> ")
    if choice == "1":
        account_manager.signUp()
    elif choice == "2":
        account_manager.logIn()
    else:
        quit()