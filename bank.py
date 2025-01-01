class BankAccount:
    def __init__(self, account_number, balance = 0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Deposit successful. New balance: {self.balance}")
        else:
            print("Deposit amount must be greater than 0.")
        

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Withdrawal successful. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be greater than 0 and less than or equal to the balance.")

    # Create accounts
account1 = BankAccount(123456)
account2 = BankAccount(234567)

# Deposit and withdraw money
account1.deposit(1000)
account1.withdraw(500)
account2.deposit(2000)
account2.withdraw(1000)

# Print account balances
print(f"Account 1 balance: {account1.balance}")
print(f"Account 2 balance: {account2.balance}")

# Output:
# Deposited 1000.0. Deposit successful. New balance: 1000.0
# Withdrawal 500.0. Withdrawal successful. New balance: 500.0
# Deposited 2000.0. Deposit successful. New balance: 2000.0
# Withdrawal 1000.0. Withdrawal successful. New balance: 1000.0
# Account 1 balance: 500.0
# Account 2 balance: 1000.0

'''
In the code above, we created a class called BankAccount. 
The class has three methods: __init__, deposit, and withdraw. The __init__ method initializes
the account number and balance of the account. The deposit method deposits money 
into the account, and the withdraw method withdraws money from the account.

'''



    