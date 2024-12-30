# create a sets of numbers

# create a set of numbers
set1 = {1, 2, 3, 4, 5, 5, 5, 5, 5, 5}
print(set1)

# sets operations
set2 = {4, 5, 6, 7, 8, 9}
print(set1 | set2)  # union
print(set1 & set2)  # intersection
print(set1 - set2)  # difference
print(set1 ^ set2)  # symmetric difference
print(set1 <= set2)  # subset
print(set1 >= set2)  # superset

# add and remove elements
set1.add(6)
print(set1)
set1.remove(6)
print(set1)
set1.discard(6)
print(set1)
set1.pop()
print(set1)
set1.clear()
print(set1)

# end of file

