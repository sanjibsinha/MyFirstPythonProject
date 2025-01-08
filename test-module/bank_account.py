# bank_account.py (BankAccount module)
from datetime import datetime

class TimeManager:
    def __init__(self):
        self.timestamps = []

    def add_timestamp(self):
        self.timestamps.append(datetime.now())

    def get_timestamps(self):
        return self.timestamps

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance  # Encapsulated balance
        self.time_manager = TimeManager()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.time_manager.add_timestamp()
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

    def get_deposit_timestamps(self):
        return self.time_manager.get_timestamps()
    
# end of bank_account.py