#!/usr/bin/python3
"""Documentation of a square class"""


class Square:
    """Class that define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """ initialze a field of a square object
        Args:
            size (int): size of the square
            position (tuple): postion
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.position = position

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

    @property
    def position(self):
        """Returns the position of the square field"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of the square object
        Args:
            value (tuple): a tuple of two integers defining the position
        Raises:
            TypeError: when the value passed is not an integer or a two integer
            tuplet
            ValueError: when the value passed is less than 0
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """print put the symbol #"""
        if self.__size == 0:
            print()
            return

        if self.__position[0] >= 0 and self.__position[1] >= 0:
            for no_pos in range(self.__position[1]):
                print()

        for r in range(self.__size):
            for spaces in range(self.__position[0]):
                print(' ', end='')
            for c in range(self.__size):
                print('#', end='')
            print()

    def __str__(self):
        """print put the symbol #"""
        if self.__size == 0:
            print()
            return

        if self.__position[0] >= 0 and self.__position[1] >= 0:
            for no_pos in range(self.__position[1]):
                print()

        for r in range(self.__size):
            for spaces in range(self.__position[0]):
                print(' ', end='')
            for c in range(self.__size):
                print('#', end='')
            print()
