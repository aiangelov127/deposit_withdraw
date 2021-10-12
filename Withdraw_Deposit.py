from datetime import date

today = date.today()

class Account:
    
    def __init__(self, balance = 0.00, account_id = str(input("what is your ID? "))):        
        self.balance = balance
        self.account_id = account_id

    def get_balance(self):
        with open(f'{self.account_id}_account.txt', 'r') as file:
            self.balance = float(file.readlines()[-1])       

    def get_user_id(self):
        with open('Accounts.txt', 'r') as file:
            accounts_list = file.read()
            list = accounts_list.split('\n')
            user_list = list
            print(user_list)
            if self.account_id in user_list:
                print(f"Your ID is {self.account_id}")
            else:
                print("No such user.")
                with open('Accounts.txt', 'a') as file:
                    file.write(f"\n{self.account_id}")
                with open(f'{self.account_id}_account.txt', 'w') as file:
                    file.write("0.00")
                print(f"Your account ID {self.account_id} was added.")
                

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
    account.get_balance()

    user_input = input("What do you want to do: deposit, withdraw or exit? ")

    if user_input == 'deposit':
        money = float(input("How much? "))
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