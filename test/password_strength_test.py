import unittest
from chalicelib.password_strength import compute_strength

class TestComputeStrength(unittest.TestCase):

    def test_empty_password(self):
        self.assertEqual(compute_strength(''), 0)

    def test_all_digits(self):
        self.assertEqual(compute_strength('123'), 2)

    def test_digits_letters(self):
        self.assertEqual(compute_strength('123a'), 4)

    def test_digits_letters_capital_letters(self):
        self.assertEqual(compute_strength('123aB'), 6)

    def test_digits_letters_capital_letters_special_symbols(self):
        self.assertEqual(compute_strength('123aB#'), 8)

    def test_digits_letters_capital_letters_special_symbols_long_enough(self):
        self.assertEqual(compute_strength('123aB#1234'), 10)

if __name__ == '__main__':
    unittest.main()