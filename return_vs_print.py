def add_two_numbers_return(a, b):
    print("This is inside the function")
    print(a + b) # Print the sum of a and b


    print("This is the return function")
    return a + b # Return the sum of a and b


result = add_two_numbers_return(5, 10)
print("This is outside the function")
print(result) # Print the result of the function

print(add_two_numbers_return(5, result)) # Print the result of the function

# Output:
# This is inside the function
# 15
# This is the return function
# This is outside the function

# 15
