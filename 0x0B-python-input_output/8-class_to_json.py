#!/usr/bin/python3
""" Module for converting objects into representation of a JSON
"""


def class_to_json(obj):
    """ Turns an object into nice representation for JSON
    Args:
        obj (object): object to transform
    """
    return(obj.__dict__)
