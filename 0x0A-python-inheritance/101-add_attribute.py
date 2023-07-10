#!/usr/bin/python3
""" Add attributes to object
"""


def add_attribute(obj, name, value):
    """ Check if the object has a __dict__ attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
