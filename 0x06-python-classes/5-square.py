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
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """return the square of the number given"""
        return self.__size ** 2

    @property
    def size(self):

        """ return the size of the square using getter
        Returns:
            size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):

        """ set the field of a square object
        Args:
            value (int): size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """print out the sqare with # symbol"""

        if self.__size <= 0:
            print()
        else:
            for i in range(self._size):
                print("#"*self.__size)
