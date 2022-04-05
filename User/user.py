
class User:
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdraw(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name},balance: {self.account_balance}")

andrew=User(name ='andrew', account_balance = '120')
josh=User(name ='josh', account_balance = '420')
sam=User(name ='sam', account_balance = '720')

andrew.make_deposit(150)
andrew.make_deposit(200)
andrew.make_deposit(50)
andrew.make_withdraw(100)
print(andrew.account_balance)

josh.make_deposit(200)
josh.make_deposit(200)
josh.make_withdraw(50)
josh.make_withdraw(150)
print(josh.account_balance)




sam.make_deposit(300)
sam.make_withdraw(20)
sam.make_withdraw(100)
sam.make_withdraw(100)
print(sam.account_balance)

andrew.display_user_balance()
josh.display_user_balance()
sam.display_user_balance()