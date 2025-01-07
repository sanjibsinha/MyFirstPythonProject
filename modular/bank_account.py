# bank_account.py (BankAccount module)
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance  # Encapsulated balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.account_number