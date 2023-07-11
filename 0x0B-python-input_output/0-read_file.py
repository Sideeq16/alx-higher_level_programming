#!/usr/bin/python3
""" Module fore reading a file """


def read_file(filename=""):
    """ Read file, filename, and prints to standard out
    Args:
        filename (str): The file to read
    """
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
