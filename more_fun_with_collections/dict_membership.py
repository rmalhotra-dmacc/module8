"""
Author: Rajiv Malhotra
Program: set_membership.py
Date: 10/14/20

Basic Dictionary Assignment
"""


def in_dict(a_dict, a_key):
    """
    Function accept a dictionary and return a boolean value stating if the element is in the dictionary.
    :param a_dict: This is a dictionary
    :param a_key: This is a key value
    :return: Boolean - True or False
    """
    return a_key in a_dict


if __name__ == '__main__':
    my_dict = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
    print("Is {} in dictionary {}? {}".format('A', my_dict, in_dict(my_dict, 'A')))
