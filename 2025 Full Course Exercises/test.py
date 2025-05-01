def factorial(num):
    """Calculate the factorial of a number."""
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def check_prime(num):
    """Check if a number is prime."""
    if num < 2:  # 0 and 1 are not prime numbers
        return False
    for i in range(2, int(num ** 0.5) + 1):
        # Check if num is divisible by i
        if num % i == 0:
            return False
    return True


def display(num):
    """Display factorial and prime status of a number."""
    print("Factorial of", num, "is", factorial(num))
    if check_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


# No need to instantiate a class, just call the function with the number
number = 10
display(number)
