# Activity Week10-2: Do decompaction for the following function With Top down for car rental System
# Decompose the following function and share your results via a GitHub link. See the function below:
'''
import datetime

def car_rental_system():
    cars = {
        "CAR001": {"type": "SUV", "available": True},
        "CAR002": {"type": "Sedan", "available": True},
        "CAR003": {"type": "Hatchback", "available": True}
    }
    users = ["user1", "user2"]
    rentals = {}

    while True:
        print("\n--- Car Rental System ---")
        print("1. View Available Cars")
        print("2. Rent a Car")
        print("3. Return a Car")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAvailable Cars:")
            for car_id, details in cars.items():
                if details["available"]:
                    print(f"{car_id} - {details['type']}")
            log_message = f"{datetime.datetime.now()} - Viewed available cars"
            with open("rental_log.txt", "a") as log_file:
                log_file.write(log_message + "\n")

        elif choice == "2":
            user_id = input("Enter your user ID: ")
            if user_id not in users:
                print("Invalid user.")
                continue

            print("\nAvailable Cars:")
            for car_id, details in cars.items():
                if details["available"]:
                    print(f"{car_id} - {details['type']}")
            car_id = input("Enter Car ID to rent: ")

            if car_id in cars and cars[car_id]["available"]:
                cars[car_id]["available"] = False
                rentals[user_id] = car_id
                print(f"{user_id} rented {car_id}")
                log_message = f"{datetime.datetime.now()} - {user_id} rented {car_id}"
                with open("rental_log.txt", "a") as log_file:
                    log_file.write(log_message + "\n")
            else:
                print("Car not available or invalid ID.")
                log_message = f"{datetime.datetime.now()} - {user_id} failed to rent {car_id}"
                with open("rental_log.txt", "a") as log_file:
                    log_file.write(log_message + "\n")

        elif choice == "3":
            user_id = input("Enter your user ID: ")
            if user_id in rentals:
                car_id = rentals[user_id]
                cars[car_id]["available"] = True
                del rentals[user_id]
                print(f"{user_id} returned {car_id}")
                log_message = f"{datetime.datetime.now()} - {user_id} returned {car_id}"
                with open("rental_log.txt", "a") as log_file:
                    log_file.write(log_message + "\n")
            else:
                print("No rental record found.")
                log_message = f"{datetime.datetime.now()} - {user_id} attempted return with no rental"
                with open("rental_log.txt", "a") as log_file:
                    log_file.write(log_message + "\n")

        elif choice == "4":
            print("Exiting system.")
            break

        else:
            print("Invalid choice.")
            log_message = f"{datetime.datetime.now()} - Invalid menu choice"
            with open("rental_log.txt", "a") as log_file:
                log_file.write(log_message + "\n")
'''


import datetime


def initialize_data():
    """Initializes cars, users, and rentals."""
    cars = {
        "CAR001": {"type": "SUV", "available": True},
        "CAR002": {"type": "Sedan", "available": True},
        "CAR003": {"type": "Hatchback", "available": True}
    }
    users = ["user1", "user2"]
    rentals = {}
    return cars, users, rentals


def log_action(message):
    """Logs actions to a file."""
    timestamp = datetime.datetime.now()
    with open("rental_log.txt", "a") as log_file:
        log_file.write(f"{timestamp} - {message}\n")


def view_available_cars(cars):
    """Displays available cars."""
    print("\nAvailable Cars:")
    for car_id, details in cars.items():
        if details["available"]:
            print(f"{car_id} - {details['type']}")
    log_action("Viewed available cars")


def rent_car(users, cars, rentals):
    """Handles car rentals."""
    user_id = input("Enter your user ID: ")
    if user_id not in users:
        print("Invalid user.")
        return

    view_available_cars(cars)
    car_id = input("Enter Car ID to rent: ")

    if car_id in cars and cars[car_id]["available"]:
        cars[car_id]["available"] = False
        rentals[user_id] = car_id
        print(f"{user_id} rented {car_id}")
        log_action(f"{user_id} rented {car_id}")
    else:
        print("Car not available or invalid ID.")
        log_action(f"{user_id} failed to rent {car_id}")


def return_car(cars, rentals):
    """Processes car returns."""
    user_id = input("Enter your user ID: ")
    if user_id in rentals:
        car_id = rentals[user_id]
        cars[car_id]["available"] = True
        del rentals[user_id]
        print(f"{user_id} returned {car_id}")
        log_action(f"{user_id} returned {car_id}")
    else:
        print("No rental record found.")
        log_action(f"{user_id} attempted return with no rental")


def main():
    """Handles main menu navigation."""
    cars, users, rentals = initialize_data()

    while True:
        print("\n--- Car Rental System ---")
        print("1. View Available Cars")
        print("2. Rent a Car")
        print("3. Return a Car")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_available_cars(cars)
        elif choice == "2":
            rent_car(users, cars, rentals)
        elif choice == "3":
            return_car(cars, rentals)
        elif choice == "4":
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")
            log_action("Invalid menu choice")


if __name__ == "__main__":
    main()
