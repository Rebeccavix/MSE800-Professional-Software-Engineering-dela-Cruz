# Activity Week 11-1: Unit-testing
# Describe the usage of unit testing in short paragraph, share your GitHub link. See the following code:

import unittest


def add(x, y):  # This is your function that simply returns the sum of x and y.
    return x + y


# This defines a test class. It inherits from unittest.TestCase, giving you access to test tools like assertEqual().
class TestMathOperations(unittest.TestCase):
    # This method inside your test class defines your actual test. Python knows it's a test because the method name starts with test_.
    def test_add(self):
        # This checks that add(2, 3) returns 5. If it doesn’t, Python will report a failure.
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)


if __name__ == '__main__':
    unittest.main()
# This is the Pythonic way to say: "Run the tests only if this file is being run directly (not imported elsewhere)."


'''
This code defines a simple function add(x, y) and uses Python’s unittest framework to verify that it works correctly by comparing expected and actual results.
When run, the program executes the tests and reports whether they pass or fail, helping catch bugs early.
'''
