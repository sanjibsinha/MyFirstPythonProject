name = 'Sanjib'
"""
This script demonstrates basic Python concepts including variables, data types, type conversion, 
arithmetic operations, string concatenation, string formatting, and type casting.

Variables:
- name: a string representing a person's name
- age: an integer representing a person's age
- height: a float representing a person's height
- is_married: a boolean indicating marital status

Functions:
- print(): outputs data to the console
- type(): returns the type of an object
- input(): reads a line from input, converts it to a string

Operations:
- Arithmetic operations: addition, subtraction, multiplication, division, floor division, modulus, exponentiation
- String concatenation: combining strings using '+' and '*'
- String formatting: using '%' operator, 'format()' method, and f-strings

Type Casting:
- Converting input string to integer using int()
"""
age = 25
height = 5.11
is_married = False

print(name)
print(age)
print(height)
print(is_married)

# type conversion
print(type(name))
print(type(age))
print(type(height))
print(type(is_married)) # boolean
print(type(True)) # boolean type

# arithmetic operations
print(2 + 3)
print(5 - 7)
print(4 * 6)
print(10 / 3)   # division
print(10 // 3)  # floor division
print(10 % 3)   # modulus   (remainder) 
print(2 ** 3)   # exponentiation
print(5 + 3 * 2) # order of operations

# string concatenation
print('Hello' + ' ' + 'World')
print('Hello' * 3)

# string formatting
print('Hello, my name is %s and I am %d years old' % (name, age))
print('Hello, my name is {} and I am {} years old'.format(name, age))
print(f'Hello, my name is {name} and I am {age} years old')

# type casting
age = int(input('Enter your age: '))
print(f'You are {age} years old')
