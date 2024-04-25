#!/usr/bin/python3

"""This module contains a class."""

class Square:
    """A class with one attribute and multiple functions."""

    def __init__(self, size=0):
        """Initialize the Square object with a size.

        Args:
            size (optional): The size of the object. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

