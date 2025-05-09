import math


class Complex:
    def __init__(self, real: float, imag: float):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    def angle(self):
        return math.atan2(self.imag, self.real)

    def magnitude(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __truediv__(self, other):
        my_theta = self.angle()
        my_r = self.magnitude()

        other_theta = other.angle()
        other_r = other.magnitude()
        if other_r == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return Complex(
            my_r / other_r * math.cos(my_theta - other_theta),
            my_r / other_r * math.sin(my_theta - other_theta),
        )


if __name__ == "__main__":
    c1 = Complex(3, 4)
    c2 = Complex(1, 2)
    print(f"c1: {c1}")
    print(f"c2: {c2}")
    print(f"c1 + c2: {c1 + c2}")
    print(f"c1 - c2: {c1 - c2}")
    print(f"c1 * c2: {c1 * c2}")
    print(f"c1 / c2: {c1 / c2}")
