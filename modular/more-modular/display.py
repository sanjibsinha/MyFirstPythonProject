from bank import Bank

my_bank = Bank("ABC Bank")
my_bank.add_customer(1, "John Doe")
customer1 = my_bank.get_customer(1)
customer1.add_account('savings', 101)
customer1.add_account('checking', 102)

savings_account = customer1.get_account(101)
savings_account.deposit(500)
# savings_account.calculate_interest()
print(f"Savings Account balance: {savings_account.get_balance()}")

checking_account = customer1.get_account(102)
checking_account.deposit(1000)
checking_account.withdraw(200) # overdraft allowed
print(f"Checking Account balance: {checking_account.get_balance()}")

print(f"Customer details: {customer1.get_customer_details()}")
print(f"Bank name: {my_bank.get_bank_name()}")

my_bank.add_customer(2, "Jane Doe")
customer2 = my_bank.get_customer(2)
customer2.add_account('savings', 201)
customer2.add_account('checking', 202)

checking_account2 = customer2.get_account(202)
checking_account2.withdraw(500) # overdraft not allowed
print(f"Checking Account balance: {checking_account2.get_balance()}")

print(f"Customer details: {customer2.get_customer_details()}")
print(f"Bank name: {my_bank.get_bank_name()}")