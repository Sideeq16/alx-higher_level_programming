#!/usr/bin/python3
""" Module for writing to files
"""


def write_file(filename="", text=""):
    """ Appends text to file end
    Args:
        filename (str): the file to append to
        text (str): the text to append
    """
    with open(filename, mode='w', encoding="UTF=8") as f:
        return(f.write(text))
