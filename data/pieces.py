from .game_logic import sum_directions
from .constants import N, S, W, E, GRID_SIZE

class Piece:
    def __str__(self):
        return self.color + self.tag
    def get_full_name(self):
        return '_'.join(['black' if self.color == 'b' else 'white', type(self).__name__.lower()])

class Pawn(Piece):
    tag = 'P'

    def __init__(self, color):
        self.color = color
        # MOVEMENT
        self.movement_range = 1
        self.movement = N if color == 'w' else S
        
        # TO DO
        # bicie w przelocie

class King(Piece):
    tag = 'K'

    def __init__(self, color):  # parametry do poprawienia
        self.color = color
        self.movement_range = 1
        self.movement = rotations(N, S, E, W) + rotations(sum_directions(N, E))

        # self.all_moves = listing_moves_for_the_piece(self.movement, self.movement_range, piece_coord)
        # TO DO
        # dodac znaczniki i ruch roszady dla bialego i czarnego

class Rook(Piece):
    tag = 'R'

    def __init__(self, color):
        self.color = color
        self.movement_range = GRID_SIZE - 1
        self.movement = rotations(N)

        # self.all_moves = listing_moves_for_the_piece(self.movement, self.movement_range, piece_coord)

class Knight(Piece):
    tag = 'N'

    def __init__(self, color):
        self.color = color
        self.movement_range = 1
        self.movement = rotations(sum_directions(N, N, E)) + rotations(sum_directions(N, N, W))

        # self.all_moves = listing_moves_for_the_piece(self.movement, self.movement_range, piece_coord)

class Bishop(Piece):
    tag = 'B'

    def __init__(self, color):
        self.color = color
        self.movement_range = GRID_SIZE - 1
        self.movement = rotations(sum_directions(N, E))

        # self.all_moves = listing_moves_for_the_piece(self.movement, self.movement_range, piece_coord)

class Queen(Piece):
    tag = 'Q'

    def __init__(self, color):
        self.color = color
        self.movement_range = GRID_SIZE - 1
        self.movement = rotations(N, S, E, W) + rotations(sum_directions(N, E))
                        
        # self.all_moves = listing_moves_for_the_piece(self.movement, self.movement_range, piece_coord)
