#!/usr/bin/python3
""" Module for creating a Student class
"""


class Student():
    """ Creates a student class
    """

    def __init__(self, first_name, last_name, age):
        """ Initializes a student
        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            age (int): age of Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns dictionary description of an instance
        Args:
            attrs (list): List of strings
                          to check for in the dict representation
        """
        my_dict = {}
        new_dict = self.__dict__
        if attrs is None:
            return new_dict
        for key, value in new_dict.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict

    def reload_from_json(self, json):
        """ Reassembles class attributes from a json text
        Args:
            json (dict): dict to parse through
        """
        for key, value in json.items():
            setattr(self, key, value)
