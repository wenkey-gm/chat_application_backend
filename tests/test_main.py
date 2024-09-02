import unittest

from src.main import Calculation


class TestCalculation(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(Calculation(2, 5).addition(), 7, "The sum is not 7")


if __name__ == '__main__':
    unittest.main()
