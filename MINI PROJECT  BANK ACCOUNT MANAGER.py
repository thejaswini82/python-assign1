#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0 for deposit.")
            return
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0 for withdrawal.")
            return

        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
        else:
            print("Insufficient funds!")

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0 for deposit.")
            return
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0 for withdrawal.")
            return

        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds!")

class BusinessAccount(Account):
    def __init__(self, account_number, balance=0, credit_limit=1000):
        super().__init__(account_number, balance)
        self.credit_limit = credit_limit

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0 for deposit.")
            return
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0 for withdrawal.")
            return

        if self.balance - amount >= -self.credit_limit:
            self.balance -= amount
        else:
            print("Insufficient funds!")

# ATM-style program to manage accounts
def atm_program():
    checking_account = CheckingAccount("C12345", 500, overdraft_limit=200)
    savings_account = SavingsAccount("S98765", 1000)
    business_account = BusinessAccount("B45678", 2000, credit_limit=500)

    while True:
        print("\n===== ATM MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            account_type = input("Enter account type (Checking/Savings/Business): ")
            amount = float(input("Enter deposit amount: "))
            if account_type.lower() == 'checking':
                checking_account.deposit(amount)
            elif account_type.lower() == 'savings':
                savings_account.deposit(amount)
            elif account_type.lower() == 'business':
                business_account.deposit(amount)
            else:
                print("Invalid account type.")
        
        elif choice == '2':
            account_type = input("Enter account type (Checking/Savings/Business): ")
            amount = float(input("Enter withdrawal amount: "))
            if account_type.lower() == 'checking':
                checking_account.withdraw(amount)
            elif account_type.lower() == 'savings':
                savings_account.withdraw(amount)
            elif account_type.lower() == 'business':
                business_account.withdraw(amount)
            else:
                print("Invalid account type.")
        
        elif choice == '3':
            account_type = input("Enter account type (Checking/Savings/Business): ")
            if account_type.lower() == 'checking':
                print("Checking Account Balance:", checking_account.get_balance())
            elif account_type.lower() == 'savings':
                print("Savings Account Balance:", savings_account.get_balance())
            elif account_type.lower() == 'business':
                print("Business Account Balance:", business_account.get_balance())
            else:
                print("Invalid account type.")

        elif choice == '4':
            print("Thank you for using the ATM. Have a nice day!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    atm_program()


# In[1]:


#2 WAY
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
        else:
            print("Insufficient funds!")

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds!")

class BusinessAccount(Account):
    def __init__(self, account_number, balance=0, credit_limit=1000):
        super().__init__(account_number, balance)
        self.credit_limit = credit_limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= -self.credit_limit:
            self.balance -= amount
        else:
            print("Insufficient funds!")

# ATM-style program to manage accounts
def atm_program():
    checking_account = CheckingAccount("C12345", 500, overdraft_limit=200)
    savings_account = SavingsAccount("S98765", 1000)
    business_account = BusinessAccount("B45678", 2000, credit_limit=500)

    # Make transactions
    checking_account.deposit(100)
    checking_account.withdraw(300)
    print("Checking Account Balance:", checking_account.get_balance())

    savings_account.withdraw(200)
    print("Savings Account Balance:", savings_account.get_balance())

    business_account.deposit(500)
    business_account.withdraw(3000)
    print("Business Account Balance:", business_account.get_balance())

if __name__ == "__main__":
    atm_program()


# In[ ]:




