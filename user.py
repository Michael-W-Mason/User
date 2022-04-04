# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def withdrawal(self, amount):
        self.balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")
    def transfer_money(self, user, amount):
        self.balance -= amount
        user.balance += amount

myself = User("Michael", 100)
someone_else = User("Nick", 200)
myself.withdrawal(50)
myself.display_user_balance()
myself.transfer_money(someone_else, 20)
myself.display_user_balance()
someone_else.display_user_balance()

