#!/usr/bin/python3
""" Module for converting from JSON
"""
import json


def from_json_string(my_str):
    """ Converts a JSON string to a Python object
    Args:
        my_str (str): a JSON string to convert
    """
    return (json.loads(my_str))
