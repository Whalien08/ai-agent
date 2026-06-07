import unittest
from pkg.calculator import calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator("3 + 5"), 8)

    def test_subtraction(self):
        self.assertEqual(calculator("10 - 4"), 6)

    def test_multiplication(self):
        self.assertEqual(calculator("4 * 3"), 12)

    def test_division(self):
        self.assertEqual(calculator("8 / 2"), 4)

    def test_precedence(self):
        self.assertEqual(calculator("3 + 7 * 2"), 17)

if __name__ == "__main__":
    unittest.main()