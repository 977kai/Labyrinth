class Labyrinth:
    """This class provides labyrinth object"""

    def __init__(self):
        self.__labyrinth = [
            ['-', '-', '-', '-', '-', '-', '-'],
            ['|', ' ', ' ', ' ', '|', ' ', 'X'],
            ['|', ' ', '|', ' ', '|', ' ', '|'],
            ['|', ' ', '|', ' ', '|', ' ', '|'],
            ['|', ' ', '|', ' ', ' ', ' ', '|'],
            ['-', '-', '-', '-', '-', '-', '-']
        ]
        self.__borders = ['-', '|']

    borders = property(lambda self: self.__borders)

    def __str__(self):
        """
        Returns:
            (str): String representation of labyrinth current state
        """
        labyrinth_str = ''
        for level in self.__labyrinth:
            labyrinth_str += ''.join(level) + '\n'
        return labyrinth_str

    def __getitem__(self, coordinates):
        """
        Return value of labyrinth cell by coords

        Args:
            coordinates (utils.Coordinates): Coordinates of labyrinth cell
        Returns:
            (str): Value of labyrinth cell
        """
        return self.__labyrinth[coordinates.y][coordinates.x]

    def update_cell(self, coordinates, value):
        """
        Update labyrinth cell with given coordinates by new value

        Args:
            coordinates (utils.Coordinates): Coordinates of labyrinth cell
            value (str): New value to be inserted into cell
        """
        self.__labyrinth[coordinates.y][coordinates.x] = value
