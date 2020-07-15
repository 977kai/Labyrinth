from labyrinth import Labyrinth
from utils import uuid, Coordinates, FinishState


class Player:
    """
    This class provides player object and methods to interact with Labyrinth

    Args:
        name (str or None): Player name
    """

    def __init__(self, name=None):
        self.__pid = name or uuid()
        self.__coords = Coordinates()
        self.__labyrinth = Labyrinth()
        self.__moves_counter = 0
        self.__finish_state = None

    def check_for_finish(self):
        """Check if player on finish"""
        if self.__labyrinth[self.__coords] == 'X':
            self.__finish_state = FinishState(self.__coords.copy(),
                                              self.__moves_counter)
            return True
        else:
            return False

    def get_finish_state(self):
        """
        If finish were found, return finish coordinates and player moves
        to find it
        """
        if self.__finish_state is not None:
            finish_coords = self.__finish_state.coords
            return {
                'x': finish_coords.x,
                'y': finish_coords.y,
                'moves': self.__finish_state.moves
            }
        return None

    def up(self):
        """Try to move player up in the labyrinth"""
        self.__moves_counter += 1
        tmp_coords = self.__coords.copy()
        tmp_coords.y -= 1
        if self.__labyrinth[tmp_coords] not in self.__labyrinth.borders:
            self.check_for_finish()
            self.__labyrinth.update_cell(tmp_coords, 'P')
            self.__labyrinth.update_cell(self.__coords, ' ')
            self.__coords.y -= 1

    def down(self):
        """Try to move player down in the labyrinth"""
        self.__moves_counter += 1
        tmp_coords = self.__coords.copy()
        tmp_coords.y += 1
        if self.__labyrinth[tmp_coords] not in self.__labyrinth.borders:
            self.check_for_finish()
            self.__labyrinth.update_cell(tmp_coords, 'P')
            self.__labyrinth.update_cell(self.__coords, ' ')
            self.__coords.y += 1

    def left(self):
        """Try to move player left in the labyrinth"""
        self.__moves_counter += 1
        tmp_coords = self.__coords.copy()
        tmp_coords.x -= 1
        if self.__labyrinth[tmp_coords] not in self.__labyrinth.borders:
            self.check_for_finish()
            self.__labyrinth.update_cell(tmp_coords, 'P')
            self.__labyrinth.update_cell(self.__coords, ' ')
            self.__coords.x -= 1

    def right(self):
        """Try to move player right at the labyrinth"""
        self.__moves_counter += 1
        tmp_coords = self.__coords.copy()
        tmp_coords.x += 1
        if self.__labyrinth[tmp_coords] not in self.__labyrinth.borders:
            self.check_for_finish()
            self.__labyrinth.update_cell(tmp_coords, 'P')
            self.__labyrinth.update_cell(self.__coords, ' ')
            self.__coords.x += 1

    def spawn(self):
        """Set initial coordinates"""
        self.__coords.x = 5
        self.__coords.y = 4
        self.__labyrinth.update_cell(self.__coords, 'P')

    def show_position(self):
        """Show labyrinth with player position in it"""
        print(self.__labyrinth)
