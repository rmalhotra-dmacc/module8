import unittest
from more_fun_with_collections import set_membership

class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        self.assertEqual(True, set_membership.in_set({43.0, 21.2, 61.0, 1}, 21.2))

    def test_in_set_false(self):
        self.assertEqual(False, set_membership.in_set({43.0, 21.2, 61.0, 1}, 33.3))


if __name__ == '__main__':
    unittest.main()
