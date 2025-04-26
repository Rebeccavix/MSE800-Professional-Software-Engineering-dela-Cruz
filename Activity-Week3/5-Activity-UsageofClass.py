# Activity W3-5: Usage of Class 
# Develop a factorial project with at least one class

class FactorialCalculator:
    """A class to calculate factorials and display results."""

    @staticmethod
    def factorial(n):
        """
        Calculate the factorial of a number using recursion.
        :param n: Non-negative integer
        :return: Factorial of the number
        """
        if n == 0 or n == 1:
            return 1
        else:
            return n * FactorialCalculator.factorial(n - 1)

    @classmethod
    def display_factorials(cls, limit):
        """
        Display factorials for numbers from 0 to the given limit.
        :param limit: Integer specifying the range
        """
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