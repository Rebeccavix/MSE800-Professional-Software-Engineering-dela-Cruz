# Activity Week11-3: Understanding Unit Testing
# Examine the following Python code that uses the unittest framework:
'''
Tasks to do:
Describe what each test method is checking.
Run the code and interpret the results.
Modify the code to add a new test case that checks if '123'.isdigit() returns True.
What happens if one of the assertions fails? Try changing one expected value and observe the result.
'''

import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        # Tests whether 'foo'.upper() returns 'FOO'
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        # Tests whether 'FOO'.isupper() is True and 'Foo'.isupper() is False
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        # Tests whether split() correctly splits a string
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        # Tests whether passing a non-string to split() raises TypeError
        with self.assertRaises(TypeError):
            s.split(2)

    def test_isdigit(self):
        # Tests whether '123'.isdigit() returns True
        self.assertTrue('123'.isdigit())


if __name__ == '__main__':
    unittest.main()
