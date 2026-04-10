#!/usr/bin/python3
"""Kvadrat klasını sahə hesablama metodu ilə təyin edir"""


class Square:
    """Kvadratı təmsil edən klas"""

    def __init__(self, size=0):
        """Kvadratın ölçüsünü yoxlayır və mənimsədir
        Args:
            size (int): Kvadratın tərəfinin ölçüsü, default 0
        Raises:
            TypeError: Əgər size integer deyilsə
            ValueError: Əgər size < 0 olarsa
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Kvadratın cari sahəsini qaytarır
        Returns:
            Kvadratın sahəsi (size * size)
        """
        return self.__size ** 2
