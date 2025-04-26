# Activity W3-5: Usage of Class 
# Develop a factorial project with at least one class

class FactorialCalculator:

    @staticmethod
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * FactorialCalculator.factorial(n - 1)

    @classmethod
    def display_factorials(cls, limit):
        for i in range(limit):  # Range starts from 0 and ends at (limit - 1)
            print(f"{i}! = {cls.factorial(i)}")


# Main program
if __name__ == "__main__":
    try:
        limit = int(input("Enter the range of numbers for factorial calculation (non-negative integer): "))
        if limit < 0:
            print("Please enter a non-negative integer.")
        else:
            FactorialCalculator.display_factorials(limit)
    except ValueError:
        print("Invalid input! Please enter a non-negative integer.")