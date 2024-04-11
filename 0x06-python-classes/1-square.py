#!/usr/bin/python3
"""This module contains a class."""


class Square:
    """A class with one attribute and multiple functions"""

    def __init__(self, size=None):
        """Initialize the Square object with a size.

        Args:
            size (optional): The size of the object. Defaults to None.
        """
        self.__size = size
