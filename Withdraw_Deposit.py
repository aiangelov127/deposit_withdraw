from datetime import date

today = date.today()

class Account:
    
    def __init__(self, account_id = str(input("what is your ID? ")), balance = 0.00):        
        self.balance = balance
        self.account_id = account_id
    
    def get_user_id(self):
        with open('Accounts.txt', 'r') as file:
            accounts_list = file.read()
            list = accounts_list.split(', ')
            user_list = list
        for num in user_list:
            if num == self.account_id:
                print(f"Your ID is {self.account_id}")
                break
            else:
                with open('Accounts.txt', 'a') as file:
                    file.write(f", {self.account_id}")
                print(f"Your account ID {self.account_id} was added.")
                break

    def log_transaction(self):
        with open(f'{self.account_id}_account.txt', 'a') as file:
            file.write(f"\n {today}: {user_input} ${money}\n {self.balance}")

    def deposit(self, money):
        self.balance = self.balance + money

    def withdraw(self, money):
        self.balance = self.balance - money


account = Account() 

while True:
    account.get_user_id()

    user_input = input("What do you want to do: deposit, withdraw or exit? ")

    if user_input == 'deposit':
        money = float(input("How much money do you want to deposit?"))
        account.deposit(money)
        account.log_transaction()
        print(f"You deposited ${money}. Your current balance is ${account.balance}")
        
    elif user_input == 'withdraw':
        money = float(input("How much money do you want to withdraw?"))
        account.withdraw(money)
        account.log_transaction()
        print(f"You withdrew ${money}. Your current balance is ${account.balance}")
    elif user_input == 'exit':
        break
    
    elif user_input != "withdraw" or user_input != "deposit":
        print("Choose a correct operation.")