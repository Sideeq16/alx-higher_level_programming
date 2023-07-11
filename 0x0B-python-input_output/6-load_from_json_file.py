#!/usr/bin/python3
""" Module to convert from JSON to Python
"""
import json


def load_from_json_file(filename):
    """ function to create an Object from a JSON file
    Args:
        filename (str): filename to read from
    """
    with open(filename, "r", encoding="UTF-8") as f:
        return (json.load(f))
