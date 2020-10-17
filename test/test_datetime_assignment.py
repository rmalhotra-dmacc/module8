import unittest
from more_fun_with_collections import datetime_assignment


class MyTestCase(unittest.TestCase):
    def test_datetime(self):
        self.assertEqual("07/01/2020", datetime_assignment.half_birthday("01/01/2020"))

    def test_datetime_incorrect(self):
        self.assertEqual("Please enter a valid date in MM/DD/YYYY format only", datetime_assignment.half_birthday("02/31/2020"))


if __name__ == '__main__':
    unittest.main()
