import unittest
from more_fun_with_collections import dict_membership


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertEqual(True, dict_membership.in_dict({'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}, 'A'))

    def test_in_dict_false(self):
        self.assertEqual(False, dict_membership.in_dict({'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}, 'X'))


if __name__ == '__main__':
    unittest.main()
