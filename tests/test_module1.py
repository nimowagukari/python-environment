import unittest
from nimowagukari_examples.module1 import add, add_double


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)


class TestAddDouble(unittest.TestCase):
    def test_add_double(self):
        self.assertEqual(add_double(3, 4), 14)


if __name__ == '__main__':
    unittest.main()
