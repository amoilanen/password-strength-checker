import unittest
from chalicelib.password_strength import compute_strength

class TestStringMethods(unittest.TestCase):

    def test_all_digits(self):
        self.assertEqual(compute_strength('123'), 0)

    def test_digits_and_some_letters(self):
        self.assertEqual(compute_strength('123a'), 1)

#TODO: Add more unit tests

if __name__ == '__main__':
    unittest.main()