# Rewrite below sample code (from activity w3-6) without using initializer & self (if it is possible?)
class Factorial:
    def factorial(num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

    def check_Prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def display(num):
        print("Factorial of", num, "is", Factorial.factorial(num))
        if Factorial.check_Prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")


Factorial.display(10)
