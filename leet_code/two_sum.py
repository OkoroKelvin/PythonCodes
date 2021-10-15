import unittest

from leet_code.TwoSum import Two_Sum


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here


def test_twoSum(self):
    # given
    two_sum = Two_Sum()
    array: list = [2, 7, 11, 13]
    target: int = 9
    # when
    actual: list = two_sum.solution(_list=array, number=target)
    expected: list = [0, 1]
    # assert
    self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
