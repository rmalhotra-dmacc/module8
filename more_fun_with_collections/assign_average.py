"""
Author: Rajiv Malhotra
Program: assign_average.py
Date: 10/16/20

Selection using Dictionary Assignment
"""


def switch_average(key):
    """
    Function to emulate case/switch functionality
    :param key: key
    :return: string
    """
    my_dict = {'A': "You entered an A!",
               'B': "You entered an B!",
               'C': "You entered an C!",
               'D': "You entered an D!",
               'F': "You entered an F!"
               }
    result = my_dict.get(key, "This is not a valid key")
    return result


if __name__ == '__main__':
    print(switch_average('A'))
