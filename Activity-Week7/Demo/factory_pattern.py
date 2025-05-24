from abc import ABC, abstractmethod

class Factory(ABC):
    
    @abstractmethod
    def create_product(self, kind=None):
        pass

class AnimalFactory(Factory):
    def __init__(self):
        pass

    def create_product(self, kind=None):
        if kind == "dog":
            animal = Dog()
        elif kind == "cat":
            animal = Cat()

        return animal

class DogFactory(Factory):
    
    def create_product(self, kind=None):
        pass

class CatFactory(Factory):
    
    def create_product(self, kind=None):
        pass

class Animals(ABC):

    @abstractmethod
    def run(self):
        pass

class Dog(Animals):

    def run(self):
        print(f"I'm a Dog, I can run!!")


class Cat(Animals):
    def __init__(self):
        pass

    def run(self):
        print(f"I'm a Cat, I can run!!")





# client
factory = DogFactory()
dog = Dog()
dog = factory.create_product()

dog.run()