
for char in "Hello, World!":
    print(char)


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(10):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(10, -1, -1):
    print(i)

# nested loop
for i in range(1, 40):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}")

        # while loop
i = 1
while i <= 10:
    print(i)
    i += 1 # i = i + 1

# avoid infinite loop
# break and continue
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print('******')

for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)


