#!/usr/bin/python3
""" List Class
"""


class MyList(list):
    """ Class that inherits from list
    """

    def print_sorted(self):
        """ Prints list in a sorted format
        """

        new_list = self[:]
        new_list.sort()
        print(new_list)
