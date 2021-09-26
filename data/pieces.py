from .functions import rotations
from .constants import *


class Piece:
    color = None
    tag = None

    def __str__(self):
        return self.color + self.tag

    def get_full_name(self):
        return '_'.join(['black' if self.color == 'b' else 'white', type(self).__name__.lower()])


class Pawn(Piece):
    tag = 'P'

    def __init__(self, color):
        self.color = color
        self.movement_range = 1
        self.movement = N if color == 'w' else S


class King(Piece):
    tag = 'K'

    def __init__(self, color):  # parametry do poprawienia
        self.color = color
        self.movement_range = 1
        self.movement = rotations(N) + rotations(NE)


class Rook(Piece):
    tag = 'R'

    def __init__(self, color):
        self.color = color
        self.movement_range = GRID_SIZE - 1
        self.movement = rotations(N)


class Knight(Piece):
    tag = 'N'

    def __init__(self, color):
        self.color = color
        self.movement_range = 1
        self.movement = rotations(NNE) + rotations(NNW)


class Bishop(Piece):
    tag = 'B'

    def __init__(self, color):
        self.color = color
        self.movement_range = GRID_SIZE - 1
        self.movement = rotations(NE)


class Queen(Piece):
    tag = 'Q'

    def __init__(self, color):
        self.color = color
        self.movement_range = GRID_SIZE - 1
        self.movement = rotations(N) + rotations(NE)
