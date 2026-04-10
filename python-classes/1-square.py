#!/usr/bin/python3
"""Kvadrat klasını ölçü ilə təyin edir"""


class Square:
    """Kvadratı təmsil edən klas"""

    def __init__(self, size):
        """Kvadratın ölçüsünü mənimsədir
        Args:
            size (int): Kvadratın tərəfinin ölçüsü
        """
        self.__size = size
