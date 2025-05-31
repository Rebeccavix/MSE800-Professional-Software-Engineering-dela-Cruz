'''Activity W8-5: Hierarchical inheritance in python
        To extend Activity W8-4, add another class named 'Cat' as a child class with a simple method to demonstrate hierarchical inheritance. Share your result with a short description here.'''

# Parent Class


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "I make a sound"

# Child Class 1


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        return "Woof!"

# Child Class 2


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        return "Meow!"


# Create instances
a = Animal("Generic Animal")
d = Dog("Buddy")
c = Cat("Whiskers")

# Test the sound method
print(f"{a.name} says: {a.sound()}")  # Output: I make a sound
print(f"{d.name} says: {d.sound()}")  # Output: Woof!
print(f"{c.name} says: {c.sound()}")  # Output: Meow!
