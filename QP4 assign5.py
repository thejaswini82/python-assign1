class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

#code to test

account = Account("Ashish", 5000)
print(account.title)   # Output: Ashish
print(account.balance)  # Output: 5000

savings_account = SavingsAccount("Ashish", 5000, 5)
print(savings_account.title)         # Output: Ashish
print(savings_account.balance)       # Output: 5000
print(savings_account.interestRate)  # Output: 5
