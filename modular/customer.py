# customer.py (Customer module)
from bank_account import BankAccount # Import the bank account module

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.accounts = {}  # Dictionary to store accounts

    def add_account(self, account_number):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number)
            return True
        return False
        
    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def get_customer_details(self):
        return f"ID: {self.customer_id}, Name: {self.name}"