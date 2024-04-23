import unittest

from main import format_coefficient, reformat


class TestFormatExpression(unittest.TestCase):
    def test_1(self):
        self.assertEqual("2x-y", reformat(0, 2, -1))
        self.assertEqual("3-2y", reformat(3, 0, -2))


if __name__ == '__main__':
    unittest.main()
