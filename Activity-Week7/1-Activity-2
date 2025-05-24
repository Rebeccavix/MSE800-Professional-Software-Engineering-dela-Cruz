# Activity Week7-1.2: Singleton Design Pattern - Follow up Question
# Is "car_name" variable is the same location in the memory?
# Debug the code to get the name of the car from end user? See below code:


class RentalManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.cars_available = ["Toyota", "Honda", "Ford"]
        return cls._instance

    def rent_car(self, car_name):
        if car_name in self.cars_available:
            self.cars_available.remove(car_name)
            print(f"{car_name} has been rented.")
        else:
            print(f"{car_name} is not available.")

    def show_available_cars(self):
        print("Available cars:", self.cars_available)


manager1 = RentalManager()
manager2 = RentalManager()

# Get car name input from the user
# Debugging step
car_name = input(
    "Enter the name of the car to rent - select and type 'Toyota', 'Honda' or 'Ford': ")

manager1.rent_car(car_name)
manager2.show_available_cars()

print("Are both managers the same object?", manager1 is manager2)
print("ID of manager1 and manager2:", id(manager1), id(manager2))
# Debugging step to check memory address of input
print("ID of car_name variable:", id(car_name))
