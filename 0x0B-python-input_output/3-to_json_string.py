#!/usr/bin/python3
""" Documentation for a function to_json_string
"""
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)
    Args:
        my_obj (object): object ot turn into JSON
    """
    return (json.JSONEncoder().encode(my_obj))
