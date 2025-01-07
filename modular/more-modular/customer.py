from accounts import SavingsAccount, CheckingAccount

class Customer:
    """A customer of ABC Bank with a checking account. Customers have the following properties:
    """

    def __init__(self, customer_id, name):
        self._customer_id = customer_id # protected attribute
        self._name = name # protected attribute
        self._accounts = { } # protected attribute and empty encapsulated dictionary

    def add_account(self, account_type, account_number):
        """Add an account of specified type"""
        if account_number in self._accounts:
            return False # account exists
        
        if account_type == 'savings':
            self._accounts[account_number] = SavingsAccount(account_number)
        elif account_type == 'checking':
            self._accounts[account_number] = CheckingAccount(account_number)
        else:
            return False # unknown account type
        
        return True # account added
    
    def get_account(self, account_number):
        """Return the account with the given account number"""
        return self._accounts.get(account_number)
    
    def get_customer_details(self):
        return f"ID: {self._customer_id}, Name: {self._name}" # "self._customer_id, self._name"
    

# end of customer.py