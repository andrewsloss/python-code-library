class BankAccount:
    def __init__(self, name, accountID, balance):
        self.name = name
        self.accountID = accountID
        self.balance = balance

    def __str__(self):
        return f"Account Name = {self.name}, Account ID = {self.accountID}, Balance = {self.balance}"

    def makeDeposit(self, dep):
        self.balance += dep
        print(f"New Balance = {self.balance}")
    
    def makeWithdraw(self, wit):
        if(self.balance - wit < 0):
            print("Insufficient Funds")
        else:
            self.balance -= wit
            print(f"New Balance = {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, name, accountID, balance, savingsBalance):
        super().__init__(name, accountID, balance)
        self.savingsBalance = savingsBalance
    
    def __str__(self):
        return f"Savings Balance = {self.savingsBalance}, Account Name = {self.name}, Account ID = {self.accountID}, Balance = {self.balance}"

    def makeSavingsDeposit(self, dep2):
        if(self.balance - dep2 < 0):
            print("Insufficient Funds")
        else:
            print(f"Old Savings Balance = {self.savingsBalance}", end = ", ")
            self.savingsBalance += dep2
            print(f"New Savings Balance = {self.savingsBalance}")
            print("Old Bank Balance = " + str(self.balance), end = ", ")
            self.makeWithdraw(dep2)

    def makeSavingsWithdraw(self, wit2):
        if(self.savingsBalance - wit2 < 0):
            print("Insufficient Funds")
        else:
            print(f"Old Savings Balance = {self.savingsBalance}", end = ", ")
            self.savingsBalance -= wit2
            print(f"New Savings Balance = {self.savingsBalance}")
            print("Old Bank Balance = " + str(self.balance), end = ", ")
            self.makeDeposit(wit2)

andrew = SavingsAccount("Andrew Sloss", "T0001", 0, 0)

while True:

    print("1. Deposit 2. Withdraw 3. Savings Deposit 4. Savings Withdraw 5. STOP CODE")
    choice = input("> ")

    if choice == "1":
        a = int(input("Deposit Amount: "))
        andrew.makeDeposit(a)
    elif choice == "2":
        b = int(input("Withdraw Amount: "))
        andrew.makeWithdraw(b)
    elif choice == "3":
        c = int(input("Savings Deposit Amount: "))
        andrew .makeSavingsDeposit(c)
    elif choice == "4":
        d = int(input("Savings Withdraw Amount: "))
        andrew.makeSavingsWithdraw(d)
    elif choice == "5":
        print("Code Stoped")
        break
    else:
        print("Not A Valid Command")