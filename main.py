#import BankAccount class from BankAccount.py
from BankAccount import BankAccount

#instantiate BankAccount with hardcoded account name and starting balance
my_account = BankAccount("Wally", 200.00)

#deposit some money into account
my_account.deposit(500.00)

#withdraw some money from account
my_account.withdraw(300.00)

#print result of calling get the_balance method
balance_info = my_account.get_balance()
print(balance_info)

#used chatgpt for help