"""
Author: Rajiv Malhotra
Program: datetime_assignment.py
Date: 10/17/20

Python datetime Assignment
"""


from datetime import datetime


def half_birthday(a_datetime):
    """
    Function calculates the half birthday (+6 months)
    :param a_datetime: Birthday in Datetime format
    :return: Half birthday in Datetime format
    """
    format_str = '%m/%d/%Y'
    try:
        a_datetime_obj = datetime.strptime(a_datetime, format_str)
    except ValueError as err:
        return "Please enter a valid date in MM/DD/YYYY format only"

    new_year = a_datetime_obj.year
    new_month = a_datetime_obj.month + 6
    if new_month > 12:
        new_year += 1
        new_month -= 12
    new_day = a_datetime_obj.day
    while True:
        try:
            new_half_birthday = datetime(new_year, new_month, new_day)
        except ValueError:
            new_day -= 1
        else:
            break
    return datetime.strftime(new_half_birthday, "%m/%d/%Y")


if __name__ == '__main__':
    birthday_str = input("Enter your birthday in MM/DD/YYYY format: ")
    print(half_birthday(birthday_str))
