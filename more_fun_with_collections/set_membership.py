"""
Author: Rajiv Malhotra
Program: set_membership.py
Date: 10/14/20

Set Assignment
"""


def in_set(some_set, some_value):
    """
    Function accepts a set and returns a boolean value stating if the element is in the set.
    :param some_set: This is a set
    :param some_value: This is a string
    :return: Boolean - True or False
    """
    return some_value in some_set


if __name__ == '__main__':
    my_set = set('0123456789')
    print("Is {} in {}? {}".format(5, my_set, in_set(my_set, str(5))))
