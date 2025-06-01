'''Activity W8-4: single inheritance in python
    Write a Python program using single inheritance.
        Create two classes: Animal (parent class) and Dog (child class).
        Add a simple method in each class to demonstrate how single inheritance works.
        After writing the code, briefly explain how it works.
        Finally, share your code and explanation here.'''

# Parent Class


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "I make a sound"

# Child Class


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        return "Woof!"


# Create instances
a = Animal("Generic Animal")
d = Dog("Buddy")

# Test the sound method
print(f"{a.name} says: {a.sound()}")  # Output: I make a sound
print(f"{d.name} says: {d.sound()}")  # Output: Woof!


# Animal class: Has a sound() method that returns "I make a sound"
# Dog class: Overrides the sound() method to return "Woof!"
