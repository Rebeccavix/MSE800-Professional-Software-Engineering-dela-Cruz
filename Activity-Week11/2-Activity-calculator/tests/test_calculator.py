import unittest
import math
import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(4, 0), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(5, 0)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)

    def test_root(self):
        self.assertEqual(calculator.root(27, 3), 3)
        with self.assertRaises(ValueError):
            calculator.root(-8, 2)

    def test_trigonometry(self):
        self.assertAlmostEqual(calculator.sin(math.pi / 2), 1.0, places=5)
        self.assertAlmostEqual(calculator.cos(0), 1.0, places=5)
        self.assertAlmostEqual(calculator.tan(math.pi / 4), 1.0, places=5)
        with self.assertRaises(ValueError):
            calculator.tan(math.pi / 2)


if __name__ == '__main__':
    unittest.main()
