#!/usr/bin/python3
"""Kvadrat klasını koordinatlarla təyin edir"""


class Square:
    """Kvadratı təmsil edən klas"""

    def __init__(self, size=0, position=(0, 0)):
        """Kvadratı təyin edir
        Args:
            size (int): Ölçü
            position (tuple): Koordinatlar
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Ölçünü qaytarır"""
        return self.__size

    @size.setter
    def size(self, value):
        """Ölçünü yoxlayır və mənimsədir"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Koordinatları qaytarır"""
        return self.__position

    @position.setter
    def position(self, value):
        """Koordinatları yoxlayır və mənimsədir"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Sahəni qaytarır"""
        return self.__size ** 2

    def my_print(self):
        """Kvadratı koordinatlara uyğun çap edir"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
