class Director:

    def construct_product(self, builder):
        builder.create_new_car()
        builder.add_engine()
        builder.add_model()
        

class Builder:

    def __init__(self):
        self.car = None
        
    def create_new_car(self):
        self.car = Car()

    def get_car(self):
        return self.car
    
class Car:
    def __init__(self):
        self.model = None
        self.engine = None

    def __str__(self):
        return f"Car model is {self.model}, car engine is {self.engine}"

class CarBuilder(Builder):

    def add_model(self):
        self.car.model = "Sport Model"
    
    def add_engine(self):
        self.car.engine = "ENGINE"


# client
director = Director()
car_builder = CarBuilder()

director.construct_product(car_builder)
car = car_builder.get_car()

print(car)
