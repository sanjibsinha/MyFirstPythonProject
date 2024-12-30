# create a dictionary and print the value of a key

# create a dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# print the value of a key
print("dict['Name']: ", dict['Name'])

# Output: dict['Name']:  Zara

# modify the key value pair
dict['Age'] = 8

# print the modified key value pair
print("dict['Age']: ", dict['Age'])

# Output: dict['Age']:  8

# add a new key value pair
dict['School'] = "DPS School"

# print the new key value pair
print("dict['School']: ", dict['School'])

# Checking if a key exists
print("Name" in dict) # Output: True

# Getting all the keys
print(dict.keys())

# Getting all the values
print(dict.values())

# Getting all the key-value pairs as tuples
print(dict.items())

# Removing a key-value pair
del dict["Name"]
print(dict)

