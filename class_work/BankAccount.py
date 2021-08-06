from class_work.User import User


class BankAccount:
    def __init__(self, account_name, account_number, account_id, account_balance, user):
        self.account_name = account_name
        self.account_number = account_number
        self.account_id = account_id
        self.account_balance = 0.00
        self.user = user

    def __str__(self):
        return f"This account is owned by {self.account_name}"

    def deposit(self, amount):
        self.account_balance += amount

    def view_balance(self):
        return self.account_balance


user1 = User("Kelvin", "08163091749", "jjju@yahoo.com")
user2 = User("Hindu", "08029281918", "jeu@yahoo.com")

account1 = BankAccount(user1.user_name, "127367287", 1, 0.00, user1)
account2 = BankAccount(user2.user_name, "123455433", 2, 0.00, user2)

account1.deposit(1000)
account2.deposit(2500)

print(account1.view_balance())




