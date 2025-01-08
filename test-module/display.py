# display.py (Main application)
from customer import Customer

customer1 = Customer("123", "Alice")
customer1.add_account("1001")
account1 = customer1.get_account("1001")

if account1:
    account1.deposit(1000)
    account1.withdraw(500)
    print(f"Account {account1.get_account_number()} balance: {account1.get_balance()}")
    print(f"Deposit timestamps: {account1.get_deposit_timestamps()}")
else:
    print("Account not found")

print(customer1.get_customer_details())

customer2 = Customer("456", "Bob")
customer2.add_account("1002")
account2 = customer2.get_account("1002")

if account2:
    account2.deposit(2000)
    print(f"Account {account2.get_account_number()} balance: {account2.get_balance()}")
    print(f"Deposit timestamps: {account2.get_deposit_timestamps()}")
else:
    print("Account not found")

print(customer2.get_customer_details())