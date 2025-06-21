# Activity Week10-2: Do decompaction for the following function With Top down for car rental System
'''
Decompose the following function and share your results via a GitHub link. 
See the function below:
 
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
#!/usr/bin/env python3
"""
Simplified Car Rental System - Single File Version
A complete car rental management system with all features in one file.
"""

import os
import datetime


class CarRentalSystem:
    def __init__(self):
        # Initialize the car rental system with default data
        # Car inventory
        self.cars = {
            "CAR001": {"type": "SUV", "available": True},
            "CAR002": {"type": "Sedan", "available": True},
            "CAR003": {"type": "Hatchback", "available": True},
            "CAR004": {"type": "Convertible", "available": True},
            "CAR005": {"type": "Truck", "available": True}
        }

        # Valid users
        self.users = ["user1", "user2", "user3", "admin"]

        # Active rentals {user_id: car_id}
        self.rentals = {}

        # Log file
        self.log_file = "rental_log.txt"

    def log_event(self, event_type, user_id, message):
        """Log an event with timestamp"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] [{event_type}] User: {user_id} - {message}"

        try:
            with open(self.log_file, "a", encoding="utf-8") as file:
                file.write(log_message + "\n")
        except IOError as e:
            print(f"Error writing to log file: {e}")

    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*40)
        print("       CAR RENTAL SYSTEM")
        print("="*40)
        print("1. View Available Cars")
        print("2. Rent a Car")
        print("3. Return a Car")
        print("4. View All Cars Status")
        print("5. View Current Rentals")
        print("6. Add New User")
        print("7. View System Stats")
        print("8. Exit")
        print("="*40)

    def view_available_cars(self):
        """Display all available cars"""
        print("\n📋 AVAILABLE CARS:")
        print("-" * 30)

        available_cars = {car_id: details for car_id, details in self.cars.items()
                          if details["available"]}

        if not available_cars:
            print("❌ No cars available at the moment.")
        else:
            for car_id, details in available_cars.items():
                print(f"🚗 {car_id} - {details['type']}")

        print(f"\nTotal available: {len(available_cars)}")
        self.log_event(
            "VIEW", "SYSTEM", f"Viewed available cars ({len(available_cars)} available)")

    def rent_car(self):
        """Handle car rental process"""
        print("\n🚗 RENT A CAR")
        print("-" * 20)

        # Get user ID
        user_id = input("Enter your user ID: ").strip()

        # Validate user
        if user_id not in self.users:
            print("❌ Invalid user ID. Please contact admin to register.")
            self.log_event("ERROR", user_id, "Invalid user attempted rental")
            return

        # Check if user already has a rental
        if user_id in self.rentals:
            current_car = self.rentals[user_id]
            car_type = self.cars[current_car]["type"]
            print(f"❌ You already have a rental: {current_car} ({car_type})")
            print("Please return your current car before renting another.")
            return

        # Show available cars
        available_cars = {car_id: details for car_id, details in self.cars.items()
                          if details["available"]}

        if not available_cars:
            print("❌ No cars available for rental at the moment.")
            return

        print("\nAvailable cars:")
        for car_id, details in available_cars.items():
            print(f"  🚗 {car_id} - {details['type']}")

        # Get car selection
        car_id = input("\nEnter Car ID to rent: ").strip().upper()

        # Validate and process rental
        if car_id in self.cars and self.cars[car_id]["available"]:
            # Update car status
            self.cars[car_id]["available"] = False
            # Record rental
            self.rentals[user_id] = car_id
            # Success message
            car_type = self.cars[car_id]["type"]
            print(f"✅ Success! {user_id} rented {car_id} ({car_type})")
            print(f"Enjoy your {car_type}! Drive safely! 🚗💨")
            # Log event
            self.log_event("RENTAL", user_id, f"Rented {car_id} ({car_type})")
        else:
            print("❌ Car not available or invalid Car ID.")
            self.log_event("ERROR", user_id,
                           f"Failed to rent {car_id} - not available")

    def return_car(self):
        """Handle car return process"""
        print("\n🔄 RETURN A CAR")
        print("-" * 20)

        # Get user ID
        user_id = input("Enter your user ID: ").strip()

        # Validate user
        if user_id not in self.users:
            print("❌ Invalid user ID.")
            self.log_event("ERROR", user_id, "Invalid user attempted return")
            return

        # Check if user has a rental
        if user_id in self.rentals:
            car_id = self.rentals[user_id]
            car_type = self.cars[car_id]["type"]

            # Process return
            self.cars[car_id]["available"] = True
            del self.rentals[user_id]

            # Success message
            print(f"✅ Success! {user_id} returned {car_id} ({car_type})")
            print("Thank you for using our service! 🙏")

            # Log event
            self.log_event("RETURN", user_id,
                           f"Returned {car_id} ({car_type})")
        else:
            print("❌ No rental record found for your user ID.")
            print("You don't have any cars to return.")
            self.log_event("ERROR", user_id,
                           "Attempted return with no active rental")

    def view_all_cars_status(self):
        """Display status of all cars in inventory"""
        print("\n📊 ALL CARS STATUS")
        print("-" * 30)

        available_count = 0
        rented_count = 0

        for car_id, details in self.cars.items():
            if details["available"]:
                status = "✅ Available"
                available_count += 1
            else:
                status = "❌ Rented"
                rented_count += 1
                # Find who rented it
                renter = next(
                    (user for user, car in self.rentals.items() if car == car_id), "Unknown")
                status += f" (by {renter})"

            print(f"🚗 {car_id} - {details['type']} - {status}")

        print(
            f"\n📈 Summary: {available_count} available, {rented_count} rented")
        self.log_event("VIEW", "SYSTEM", "Viewed all cars status")

    def view_current_rentals(self):
        """Display all current rental information"""
        print("\n📋 CURRENT RENTALS")
        print("-" * 25)

        if not self.rentals:
            print("✅ No active rentals at the moment.")
        else:
            for user_id, car_id in self.rentals.items():
                car_type = self.cars[car_id]["type"]
                print(f"👤 User: {user_id} ➡️ 🚗 Car: {car_id} ({car_type})")

        print(f"\nTotal active rentals: {len(self.rentals)}")
        self.log_event("VIEW", "SYSTEM",
                       f"Viewed current rentals ({len(self.rentals)} active)")

    def add_new_user(self):
        """Add a new user to the system"""
        print("\n👤 ADD NEW USER")
        print("-" * 20)

        new_user = input("Enter new user ID: ").strip()

        if not new_user:
            print("❌ User ID cannot be empty.")
            return

        if new_user in self.users:
            print(f"❌ User '{new_user}' already exists.")
        else:
            self.users.append(new_user)
            print(f"✅ User '{new_user}' added successfully!")
            self.log_event("ADMIN", "SYSTEM", f"Added new user: {new_user}")

    def view_system_stats(self):
        """Display system statistics"""
        print("\n📊 SYSTEM STATISTICS")
        print("-" * 30)

        # Car statistics
        total_cars = len(self.cars)
        available_cars = sum(
            1 for car in self.cars.values() if car["available"])
        rented_cars = total_cars - available_cars

        # User statistics
        total_users = len(self.users)
        active_renters = len(self.rentals)

        # Car type breakdown
        car_types = {}
        for car in self.cars.values():
            car_types[car["type"]] = car_types.get(car["type"], 0) + 1

        print(
            f"🚗 Cars: {total_cars} total, {available_cars} available, {rented_cars} rented")
        print(
            f"👥 Users: {total_users} registered, {active_renters} currently renting")

        print(f"\n🏷️ Car Types:")
        for car_type, count in car_types.items():
            print(f"   {car_type}: {count}")

        # Log file stats
        try:
            if os.path.exists(self.log_file):
                with open(self.log_file, "r") as f:
                    log_lines = len(f.readlines())
                print(f"\n📝 Log entries: {log_lines}")
            else:
                print(f"\n📝 Log entries: 0 (log file not created yet)")
        except:
            print(f"\n📝 Log entries: Unable to read log file")

        self.log_event("VIEW", "SYSTEM", "Viewed system statistics")

    def run(self):
        """Main application loop"""
        print("🚗 Welcome to the Car Rental System! 🚗")
        print("Your one-stop solution for car rentals!")

        while True:
            try:
                self.display_menu()
                choice = input("Enter your choice (1-8): ").strip()

                if choice == "1":
                    self.view_available_cars()
                elif choice == "2":
                    self.rent_car()
                elif choice == "3":
                    self.return_car()
                elif choice == "4":
                    self.view_all_cars_status()
                elif choice == "5":
                    self.view_current_rentals()
                elif choice == "6":
                    self.add_new_user()
                elif choice == "7":
                    self.view_system_stats()
                elif choice == "8":
                    print("\n🙏 Thank you for using Car Rental System!")
                    print("Drive safely and have a great day! 🚗💨")
                    self.log_event("SYSTEM", "SYSTEM", "System shutdown")
                    break
                else:
                    print("❌ Invalid choice. Please enter a number between 1-8.")
                    self.log_event("ERROR", "SYSTEM",
                                   f"Invalid menu choice: {choice}")

                # Pause for user to read output
                input("\nPress Enter to continue...")

            except KeyboardInterrupt:
                print("\n\n🛑 System interrupted by user.")
                self.log_event("SYSTEM", "SYSTEM",
                               "System interrupted (Ctrl+C)")
                break
            except Exception as e:
                print(f"❌ An unexpected error occurred: {e}")
                self.log_event("ERROR", "SYSTEM",
                               f"Unexpected error: {str(e)}")


def main():
    """Main function to run the car rental system"""
    system = CarRentalSystem()
    system.run()


if __name__ == "__main__":
    main()
