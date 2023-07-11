#!/usr/bin/python3
""" Module for converting into JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object into a text file, using a JSON representation
    Args:
        my_obj (object): object to turn into JSON
        filename (str): file to write into
    """
    with open(filename, "w+", encoding="UTF-8") as f:
        f.write(json.dumps(my_obj))
