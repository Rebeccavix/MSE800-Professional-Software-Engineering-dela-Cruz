# Activity W3-6: Expand your previous project (Activity W3-5) with adding prime functionality
# Develop a project to get a number from end user to calculate the factorial and checking prime using classes.

# Define a class to perform operations on a number
class NumberOperations:
    def __init__(self, number):
        self.number = number

    def factorial(self):
        if self.number < 0:
            return None  # Factorial is not defined for negative numbers
        result = 1
        for i in range(1, self.number + 1):
            result *= i
        return result

    def is_prime(self):
        if self.number <= 1:
            return False
        for i in range(2, int(self.number ** 0.5) + 1):
            if self.number % i == 0:
                return False
        return True

# Define a function to interact with the user
def main():
    try:
        num = int(input("Enter a number: "))
        operations = NumberOperations(num)

        # Calculate and display factorial
        fact = operations.factorial()
        if fact is not None:
            print(f"The factorial of {num} is: {fact}")
        else:
            print("Factorial is not defined for negative numbers.")

        # Check and display prime status
        if operations.is_prime():
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")

    except ValueError:
        print("Invalid input. Please enter an integer.")

# Run the program
if __name__ == "__main__":
    main()
