import time
import math

# Basic method

def is_prime_basic(n):
    """Checks if n is prime using basic iteration."""
    if n <= 1:
        return False
    for i in range(2, n):  # Iterate from 2 to n-1
        if n % i == 0:
            return False
    return True

# Example usage and timing
num = 100003  # A relatively large prime number
start_time = time.time()
is_prime_basic(num)
end_time = time.time()
print(f"Basic method for {num}: Time taken = {end_time - start_time:.6f} seconds")

num = 100000007 # A larger prime number
start_time = time.time()
is_prime_basic(num)
end_time = time.time()
print(f"Basic method for {num}: Time taken = {end_time - start_time:.6f} seconds")

# Optimized method

def is_prime_optimized(n):
    """
    Checks if a number is prime using an optimized algorithm.
    This function uses an optimization technique that checks divisibility 
    up to the square root of the number, skipping even numbers and multiples of 3.
    Parameters:
        n (int): The number to check for primality.
    Returns:
        bool: True if the number is prime, False otherwise.
    Examples:
        >>> is_prime_optimized(11)
        True
        >>> is_prime_optimized(25)
        False
    """

    """Checks if n is prime using optimization (checking up to sqrt(n))."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6): # Optimized loop
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# Example usage and timing
num = 100003  # A relatively large prime number
start_time = time.time()
is_prime_optimized(num)
end_time = time.time()
print(f"Optimized method for {num}: Time taken = {end_time - start_time:.6f} seconds")

num = 100000007 # A larger prime number
start_time = time.time()
is_prime_optimized(num)
end_time = time.time()
print(f"Optimized method for {num}: Time taken = {end_time - start_time:.6f} seconds")

'''
Basic method for 100003: Time taken = 0.012857 seconds
Basic method for 100000007: Time taken = 8.929559 seconds

key diffrences between basic and optimized method is that in optimized method we are 
checking divisibility up to the square root of the number, skipping even numbers and multiples of 3.

Optimized method for 100003: Time taken = 0.000027 seconds
Optimized method for 100000007: Time taken = 0.000385 seconds
'''