#!/usr/bin/python3
"""Kvadrat klasını getter və setter ilə təyin edir"""


class Square:
    """Kvadratı təmsil edən klas"""

    def __init__(self, size=0):
        """Kvadratı təyin edir
        Args:
            size (int): Kvadratın ölçüsü
        """
        self.size = size

    @property
    def size(self):
        """Kvadratın ölçüsünü qaytarır (Getter)"""
        return self.__size

    @size.setter
    def size(self, value):
        """Kvadratın ölçüsünü yoxlayır və mənimsədir (Setter)
        Args:
            value (int): Yeni ölçü dəyəri
        Raises:
            TypeError: Əgər value integer deyilsə
            ValueError: Əgər value < 0 olarsa
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın sahəsini qaytarır"""
        return self.__size ** 2
