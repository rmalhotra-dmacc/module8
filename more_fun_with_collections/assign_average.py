"""
Author: Rajiv Malhotra
Program: assign_average.py
Date: 10/16/20

Selection using Dictionary Assignment
"""


def a_grade():
    return "You entered an A!"


def b_grade():
    return "You entered an B!"


def c_grade():
    return "You entered an C!"


def d_grade():
    return "You entered an D!"


def f_grade():
    return "You entered an F!"


def switch_average(key):
    """
    Function to emulate case/switch functionality
    :param key: key
    :return: string
    """
    my_dict = {'A': a_grade,
               'B': b_grade,
               'C': c_grade,
               'D': d_grade,
               'F': f_grade
               }
    func = my_dict.get(key, lambda: "This is not a valid key")
    return func()


if __name__ == '__main__':
    print(switch_average('A'))
