def greet(name):
    """
    Greet a person with a hello message.
    Args:
        name (str): The name of the person to greet.
    Returns:
        str: A greeting message.
    """

    return f'Hello, {name}!'

print(greet('Sanjib')) # greet('Hello Sanjib')

def add(a, b):
    """
    Adds two numbers together.
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    Returns:
        int or float: The sum of the two numbers.
    """
    
    return a + b

print(add(2, 3)) # add(2, 3)

def subtract(a, b):
    """
    Subtracts two numbers.
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    Returns:
        int or float: The difference between the two numbers.
    """
    
    return a - b    

print(subtract(5, 3)) # subtract(5, 3)

def multiply(a, b):
    """
    Multiplies two numbers.
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    Returns:
        int or float: The product of the two numbers.
    """
    
    return a * b

print(multiply(2, 3)) # multiply(2, 3)

# end of func.py