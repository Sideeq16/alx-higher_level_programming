#!/usr/bin/python3
""" check object types
"""


def is_kind_of_class(obj, a_class):
    """ Function that checks if obj is an instance of,
        or check if the object is an instance of a class that he inherited from,
        the specified class
    Args:
        obj (object): the object to test
        a_class (class): the class to see if object is a part of
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
