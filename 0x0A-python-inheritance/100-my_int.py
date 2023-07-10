#!/usr/bin/python3
""" Reverse integer module
"""


class MyInt(int):
    """ Class MyInt that inherits from int
        Uses comparisons on numbers passed
    """
    def __eq__(self, other):
        """ Method that calls not equals in int super class
        Args:
            other (int): the integer to compare to
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Method that calls equals in int super class
        Args:
            other (int): the integer to compare to
        """
        return super().__eq__(other)
