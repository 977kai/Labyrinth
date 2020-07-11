class Labyrinth:
    """This class provides labyrinth object"""

    def __init__(self):
        self._labyrinth = [
            ['-', '-', '-', '-', '-', '-', '-'],
            ['|', ' ', ' ', ' ', '|', ' ', 'X'],
            ['|', ' ', '|', ' ', '|', ' ', '|'],
            ['|', ' ', '|', ' ', '|', ' ', '|'],
            ['|', ' ', '|', ' ', ' ', ' ', '|'],
            ['-', '-', '-', '-', '-', '-', '-']
        ]

    def __str__(self):
        """
        Returns:
            (str): String representation of labyrinth current state
        """
        labyrinth_str = ''
        for level in self._labyrinth:
            labyrinth_str += ''.join(level) + '\n'
        return labyrinth_str

    def update_cell(self, coordinates, value):
        """
        Update labyrinth cell with given coordinates by new value

        Args:
            coordinates (tuple of int): (x, y) coordinates of labyrinth cell
            value (str): New value to be inserted into cell
        """
        self._labyrinth[coordinates[1]][coordinates[0]] = value
