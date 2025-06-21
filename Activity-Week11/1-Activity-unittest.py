# Activity Week 11-1: Unit-testing
# Describe the usage of unit testing in short paragraph, share your GitHub link. See the following code:

import unittest


def add(x, y):
    return x + y


class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)


if __name__ == '__main__':
    unittest.main()


'''
Testing whether the add function returns the correct results.
This is part of something called Test-Driven Development (TDD), 
where you write small tests to make sure each piece of your code works as expected.
'''
