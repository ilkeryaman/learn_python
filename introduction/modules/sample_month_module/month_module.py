"""
NOTE: To register your own module as global, you should put module file inside Lib folder of Python installation.
"""
from . import months


def get_month_by_index(index):
    """
    Returns short name of month by index
    """
    if 0 <= index <= 11:
        print("Selected month is: {}".format(months[index]))
    else:
        raise ValueError("Invalid index")


def get_month_by_order(order):
    """
    Returns short name of month by order
    """
    if 1 <= order <= 12:
        print("Selected month is: {}".format(months[order-1]))
    else:
        raise ValueError("Invalid order")


