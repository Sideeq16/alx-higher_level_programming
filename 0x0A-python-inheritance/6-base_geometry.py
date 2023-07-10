#!/usr/bin/python3
""" Module for geometry
"""


class BaseGeometry():
    """ Base class
    """
    def area(self):
        """ Method that raises an exception on error
        """
        raise Exception("area() is not implemented")
