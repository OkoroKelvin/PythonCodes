import unittest

from chapter2.get_length import get_length


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_length_is_1(self):
        result = get_length([1])
        self.assertEqual(result, 1)

    def test_get_length_is_3(self):
        result = get_length([1, 2, 3])
        self.assertEqual(result, 3)

    def test_get_length_is_5(self):
        result = get_length([1, 2, 3, 4, 7])
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
