# create a list of different data types
data_types = [1, 2.5, 'hello', True, None]
print(data_types)

# access the first element of the list
print(data_types[0])
print(data_types[1])

# access the last element of the list
print(data_types[-1])


# access the first three elements of the list
print(data_types[0:3])


# access the last three elements of the list
print(data_types[-3:])


# modify the second element of the list
data_types[1] = 3.5
print(data_types)

# add a new element to the end of the list
data_types.append(False)
print(data_types)

# add a new element to the beginning of the list
data_types.insert(0, 'world')
print(data_types)

