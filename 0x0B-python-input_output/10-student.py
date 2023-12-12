#!/usr/bin/python3
"""Defining a class student"""


class Student:
    """Initializing the class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method returning dict representation of Student"""
        return self.__dict__

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        If attrs is a list of strings,
        only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
