import unittest
from nimowagukari_examples_ext1.module1 import double


class TestDouble(unittest.TestCase):
    def test_double(self):
        self.assertEqual(double(3), 6)


if __name__ == '__main__':
    unittest.main()
