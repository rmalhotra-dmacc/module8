import unittest
from more_fun_with_collections import assign_average


class MyTestCase(unittest.TestCase):
    def test_A(self):
        self.assertEqual("You entered an A!", assign_average.switch_average('A'))


if __name__ == '__main__':
    unittest.main()
