from customer import Customer

class Bank:
    """A bank managing customers and accounts"""
    def __init__(self, name):
        self._name = name # protected attribute
        self._customers = {} # protected attribute and empty encapsulated dictionary

    def add_customer(self, customer_id, name):
        if customer_id in self._customers:
            return False # customer already exists
        self._customers[customer_id] = Customer(customer_id, name)
        return True # customer added
    
    def get_customer(self, customer_id):
        return self._customers.get(customer_id)
    
    def get_bank_name(self): 
        return self._name
    
# end of bank.py