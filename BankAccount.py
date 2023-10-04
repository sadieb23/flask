class BankAccount:
    def __init__(self, account_name, starting_balance):
        #initializes instance fields
        self.account_name = account_name
        self.balance = starting_balance

    def deposit(self, amount):
        #deposits money into account
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        #withdraws money from account
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_balance(self):
        #returns string representing the account balance
        return f"{self.account_name} has a balance of {self.balance}"
#used chatgpt for help