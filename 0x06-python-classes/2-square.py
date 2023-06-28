#!/usr/bin/python3
"""Documentation of a square class"""


class Square:
    """Class that define a square"""

    def __init__(self, size=0):
        """ initialze a field of a square object
        Args:
            size (int): size of the square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
