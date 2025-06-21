import pytest
from mypackage.calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


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
