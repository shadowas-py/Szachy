from .game_logic import sum_directions
from .constants import N, S, W, E, GRID_SIZE


class Piece:
    def __str__(self):
        return self.color + self.tag


class Pawn(Piece):
    tag = 'P'

    def __init__(self, color):  # domyslna ilosc pól o jakie dana figura moze sie poruszac
        self.color = color
        # MOVEMENT
        self.movement_range = 1
        if self.color == 'b':
            self.file_name = 'black_pawn'
        else:
            self.file_name = 'white_pawn'
        # TO DO
        # bicie w przelocie


class King(Piece):
    tag = 'K'

    def __init__(self, color):  # parametry do poprawienia
        self.color = color
        self.movement_range = 1
        self.movement = N, S, E, W,\
                        sum_directions(N, E), sum_directions(N, W), \
                        sum_directions(S, E), sum_directions(S, W),
        self.additional_movement = sum_directions(W, W), (sum_directions(E, E))# castling

        self.castling_flags = [True, True]#Short #Long
        if self.color == 'b':
            self.file_name = 'black_king'
        else:
            self.file_name = 'white_king'
        # self.all_moves = listing_moves_for_the_piece(self.movement, self.movement_range, piece_coord)
        # TO DO
        # dodac znaczniki i ruch roszady dla bialego i czarnego


class Rook(Piece):
    tag = 'R'

    def __init__(self, color):
        self.color = color
        self.movement_range = GRID_SIZE - 1
        self.movement = N, S, E, W

        # GRAPHIC
        if self.color == 'b':
            self.file_name = 'black_rook'
        else:
            self.file_name = 'white_rook'
        # self.all_moves = listing_moves_for_the_piece(self.movement, self.movement_range, piece_coord)


class Knight(Piece):
    tag = 'N'

    def __init__(self, color):
        self.color = color
        self.movement_range = 1
        self.movement = sum_directions(N, N, E), sum_directions(N, N, W), \
                        sum_directions(E, E, N), sum_directions(E, E, S), \
                        sum_directions(W, W, N), sum_directions(W, W, S), \
                        sum_directions(S, S, E), sum_directions(S, S, W)

        if self.color == 'b':
            self.file_name = 'black_knight'
        else:
            self.file_name = 'white_knight'

        # self.all_moves = listing_moves_for_the_piece(self.movement, self.movement_range, piece_coord)


class Bishop(Piece):
    tag = 'B'

    def __init__(self, color):
        self.color = color
        self.movement_range = GRID_SIZE - 1
        self.movement = sum_directions(N, E), sum_directions(N, W), \
                        sum_directions(S, E), sum_directions(S, W)

        if self.color == 'b':
            self.file_name = 'black_bishop'
        else:
            self.file_name = 'white_bishop'
        # self.all_moves = listing_moves_for_the_piece(self.movement, self.movement_range, piece_coord)


class Queen(Piece):
    tag = 'Q'

    def __init__(self, color):
        self.color = color
        self.movement_range = GRID_SIZE - 1
        self.movement = N, S, E, W, sum_directions(N, E), sum_directions(N, W), \
                        sum_directions(S, E), sum_directions(S, W)
        if self.color == 'b':
            self.file_name = 'black_queen'
        else:
            self.file_name = 'white_queen'
        # self.all_moves = listing_moves_for_the_piece(self.movement, self.movement_range, piece_coord)
