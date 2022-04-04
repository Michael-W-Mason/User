# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def withdrawal(self, amount):
        self.balance -= amount
    def deposit(self, amount):
        self.balance += amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")
    def transfer_money(self, user, amount):
        self.balance -= amount
        user.balance += amount

myself = User("Michael", 100)
someone_else = User("Nick", 200)
someone_new = User("Gary", 5)

myself.deposit(50)
myself.deposit(20)
myself.deposit(10)
myself.withdrawal(80)
myself.display_user_balance()

someone_else.deposit(100)
someone_else.deposit(20)
someone_else.withdrawal(40)
someone_else.withdrawal(50)
someone_else.display_user_balance()

someone_new.deposit(1000)
someone_new.withdrawal(40)
someone_new.withdrawal(40)
someone_new.withdrawal(40)
someone_new.display_user_balance()

myself.transfer_money(someone_new, 20)
myself.display_user_balance()
someone_new.display_user_balance()

