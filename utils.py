from uuid import uuid4
from copy import copy


def uuid():
    """
    Returns:
        (str): String from generated uuid4 without '-' characters
    """
    return str(uuid4()).replace('-', '')


class Coordinates:
    """
    A support class represents coordinates as object

    Args:
        x (int): 'x' coordinate
        y (int): 'y' coordinate
    """

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, new_x):
        new_x_type = type(new_x)
        if type(new_x_type) != int.__class__:
            raise TypeError('New "x" value must be integer, but {} passed'.
                            format(new_x_type))
        self.__x = new_x

    @y.setter
    def y(self, new_y):
        new_y_type = type(new_y)
        if type(new_y_type) != int.__class__:
            raise TypeError('New "y" value must be integer, but {} passed'.
                            format(new_y_type))
        self.__y = new_y

    def __str__(self):
        return 'x: {}\ny: {}\n'.format(self.__x, self.__y)

    def copy(self):
        return copy(self)


class FinishState:
    """
    A class to memorize finish state for player

    Args:
        coords (Coordinates): finish coordinates
        moves (int): Number of player moves before finish
    """

    def __init__(self, coords, moves):
        self.__coords = coords
        self.__moves = moves

    @property
    def coords(self):
        return self.__coords.copy()

    @property
    def moves(self):
        return self.__moves
