class Account:
    def __init__(self, account_name, account_number, account_id, account_balance):
        self.account_name = account_name
        self.account_number = account_number
        self.account_id = account_id
        self.account_balance = account_balance

    def __str__(self):
        return f"This account is owned by {self.account_name}"

    def check_balance(self):
        return self.account_balance

    def deposit(self, amount):
        self.account_balance += amount


account1 = Account("John Doe", "002938442", "1", 0.00)

print("Initial Balance ===", account1.check_balance())
account1.deposit(20.00)
print("Current Balance ===", account1.check_balance())
