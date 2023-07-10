#!/usr/bin/python3
""" function to check available attributes for param """


def lookup(obj):
    """ function returns the available attributes and methods of an object
    Args:
        obj (object): The object to check
    """
    return dir(obj)
