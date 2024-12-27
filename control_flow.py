# control flow
"""
This module demonstrates basic control flow structures in Python, including:

1. if-else statements
2. if-elif-else statements
3. Nested if-else statements

Examples:
    # if-else example

    # if-elif-else example

    # nested if-else example
"""
# if else
# if elif else
# nested if else    


# if else
a = 10
b = 20  
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    

# if elif else

a = 10
b = 20
c = 30  
if a > b:
    print("a is greater than b")    
elif b > c:
    print("b is greater than c")    
else:
    print("c is greater than a and b")  

# nested if else    
a = 10
b = 20
c = 30
if a > b:
    print("a is greater than b")
    if b > c:
        print("b is greater than c")
    else:
        print("c is greater than b")    
else:
    print("b is greater than a")
    if a > c:
        print("a is greater than c")
    else:
        print("c is greater than a")        

# end of control_flow.py