class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tricks = []

    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    def add_trick(self, trick):
        self.tricks.append(trick)

    def get_tricks(self):
        return self.tricks
    
    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet!")
            return
        print(f"{self.name} knows the following tricks:")
        for trick in self.tricks:
            print(trick)

# creating a dog object

dog1 = Dog("Buddy", 2)

# calling the bark method
dog1.bark() # Dog.bark(dog1)

# calling the birthday method
dog1.birthday()

# getting the age of the dog
print(dog1.get_age())

# setting the age of the dog
dog1.set_age(3)

# getting the age of the dog
print(dog1.get_age())

# adding a trick to the dog
dog1.add_trick("sit")

# getting the tricks of the dog
print(dog1.get_tricks())

# showing the tricks of the dog
dog1.show_tricks()

# adding another trick to the dog
dog1.add_trick("roll over")

# showing the tricks of the dog
dog1.show_tricks()

# Output
# Buddy says woof!
# 3
# 3
# ['sit']
# Buddy knows the following tricks:
# sit

'''

In the above code, we have created a Dog class with the following methods:

__init__: This is the constructor method that initializes the name and age of the dog.
bark: This method prints the sound that the dog makes.
birthday: This method increments the age of the dog by 1.
get_age: This method returns the age of the dog.
set_age: This method sets the age of the dog to a specified value.
add_trick: This method adds a trick to the list of tricks that the dog knows.
get_tricks: This method returns the list of tricks that the dog knows.
show_tricks: This method prints the tricks that the dog knows.

'''

    