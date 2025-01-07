# Module : Accounts accounts.py
from abc import ABC, abstractmethod

class Account(ABC):
    """Abstract class for account"""
    def __init__(self, account_number):
        self._account_number = account_number # protected attribute
        self._balance = 0 # protected attribute

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number
    
class SavingsAccount(Account):
    """Savings account class"""
    def __init__(self, account_number, interest_rate = 0.01):
        super().__init__(account_number)
        self._interest_rate = interest_rate # protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
class CheckingAccount(Account):
    """Checking account class"""
    def __init__(self, account_number, overdraft_limit = 0):
        super().__init__(account_number)
        self._overdraft_limit = overdraft_limit # protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance + self._overdraft_limit:
            self._balance -= amount
            return True
        return False
    
# end of accounts.py