# Activity Week7-2: Factory Pattern
# Start with reading the code to debug and then explain why the model is following Factory pattern.
# See below:


from abc import ABC, abstractmethod

# Explain Code | Generate Tests | Generate Docstrings | Ask Sourcecy


class Factory(ABC):

    @abstractmethod
    def create_product(self, kind=None):
        pass

# Explain Code | Generate Tests | Generate Docstrings | Ask Sourcecy


class AnimalFactory(Factory):
    def __init__(self):
        pass

    def create_product(self, kind=None):
        if kind == "dog":
            animal = Dog()
        elif kind == "cat":
            animal = Cat()

        return animal

# Explain Code | Generate Tests | Generate Docstrings | Ask Sourcecy


class DogFactory(Factory):

    def create_product(self, kind=None):
        pass

# Explain Code | Generate Tests | Generate Docstrings | Ask Sourcecy


class CatFactory(Factory):

    def create_product(self, kind=None):
        pass

# Explain Code | Generate Tests | Generate Docstrings | Ask Sourcecy


class Animals(ABC):

    @abstractmethod
    def run(self):
        pass

# Explain Code | Generate Tests | Generate Docstrings | Ask Sourcecy


class Dog(Animals):

    def run(self):
        print(f"I'm a Dog, I can run!!")

# Explain Code | Generate Tests | Generate Docstrings | Ask Sourcecy


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
