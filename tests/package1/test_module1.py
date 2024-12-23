import unittest
from nimowagukari_examples.package1.module1 import repeat


class TestRepeat(unittest.TestCase):
    def test_repeat(self):
        self.assertEqual(repeat("hoge"), "hogehoge")


if __name__ == '__main__':
    unittest.main()
