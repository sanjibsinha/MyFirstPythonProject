class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number # protected attribute
        self.__balance = balance # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
account = BankAccount(12345, 500)
account.deposit(100)
account.withdraw(50)
print(account.get_balance()) # Output: 550

# print(account.__balance) # This will raise an error

# The BankAccount class has two attributes: account_number and balance. The account_number attribute is protected, while the balance attribute is private. The class has three methods: deposit(), withdraw(), and get_balance(). The deposit() method adds the specified amount to the balance, the withdraw() method subtracts the specified amount from the balance if the balance is sufficient, and the get_balance() method returns the current balance. The main program creates an instance of the BankAccount class and calls the deposit() and withdraw() methods to deposit and withdraw money from the account. The output shows the current balance of the account.
# end of the program
