# Activity Week 11-2: Develop a Unit Testing Plan
# Develop a unit testing plan for the following project: a command-line engineering calculator that includes the four basic arithmetic operations, power, root, and trigonometric functions (sine, cosine, and tangent).
# Share the GitHub link including the code and short description.

import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b): return a ** b


def root(a, b):
    if a < 0 and b % 2 == 0:
        raise ValueError("Cannot take even root of negative number.")
    return a ** (1 / b)


def sin(x): return math.sin(x)
def cos(x): return math.cos(x)


def tan(x):
    if math.isclose(math.cos(x), 0, abs_tol=1e-9):
        raise ValueError("tan(x) is undefined at this angle.")
    return math.tan(x)
