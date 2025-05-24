# Activity Week7-2: Factory Pattern
# Start with reading the code to debug and then explain why the model is following Factory pattern.
# See below:

from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def create_product(self, kind=None):
        pass


class AnimalFactory(Factory):
    def create_product(self, kind=None):
        if kind == "dog":
            return Dog()
        elif kind == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")


class Animals(ABC):
    @abstractmethod
    def run(self):
        pass


class Dog(Animals):
    def run(self):
        print("I'm a Dog, I can run!")


class Cat(Animals):
    def run(self):
        print("I'm a Cat, I can run!")


# Client code
factory = AnimalFactory()
dog = factory.create_product("dog")  # Corrected method call
dog.run()

cat = factory.create_product("cat")
cat.run()

# The AnimalFactory class handles object creation, ensuring that Dog and Cat instances are created without requiring the client code to instantiate them directly.
# New animal types can easily be added to AnimalFactory without modifying existing client code, promoting scalability.
# The Factory pattern abstracts away the creation logic, allowing the client to request an object without knowing its exact implementation.
