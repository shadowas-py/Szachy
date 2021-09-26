from .functions import rotations, multiply_direction
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
        direction = N if color == 'w' else S
        self.movement = list(map(lambda it: (it, False, _pawnDiagonalCondition, _pawnDiagonalConsequence), [(1, direction), (-1, direction)]))
        self.movement.append((direction, False, _pawnForwardCondition, None))
        self.movement.append((direction, False, _pawnDoubleForwardCondition, None))

def _pawnDiagonalCondition(gameState, piece, coord, new_coord):
    return (gameState.board[new_coord[1]][new_coord[0]] is not None and gameState.board[new_coord[1]][new_coord[0]].color != piece.color) or gameState.en_passant_coord == new_coord

def _pawnDiagonalConsequence(gameState, piece, coord, new_coord):
    if gameState.en_passant_coord == new_coord:
        gameState.board[coord[1]][new_coord[0]] = None

def _pawnForwardCondition(gameState, piece, coord, new_coord):
    return gameState.board[new_coord[1]][new_coord[0]] is None

def _pawnForwardConsequence(gameState, piece, coord, new_coord):
    if coord[1] == (0 if piece_selected.color == GRID_SIZE-1):
        gameState.board[new_coord[1]][new_coord[0]] = pawn_promotion(player_color=piece.color)

def _pawnDoubleForwardCondition(gameState, piece, coord, new_coord):
    return gameState.board[new_coord[1]][new_coord[0]] is None and gameState.board[(new_coord[1]+coord[1])//2][new_coord[0]] is None and coord[1] == (6 if piece.color == 'w' else 1)

def _pawnDoubleForwardConsequence(gameState, piece, coord, new_coord):
    gameState.en_passant_coord = (new_coord[0], (new_coord[1]+coord[1])//2)

class King(Piece):
    tag = 'K'

    def __init__(self, color):  # parametry do poprawienia
        self.color = color
        self.movement = list(map(lambda it: (it, False, None, _kingMoveConsequence), rotations(N) + rotations(NE)))
        self.movement.append((WW, False, self._castlingCondition, self._castlingConsequence))
        self.movement.append((EE, False, self._castlingCondition, self._castlingConsequence))

def _kingMoveConsequence(gameState, piece, coord, new_coord):
    gameState.castling_flags[piece.color + '_short'] = False
    gameState.castling_flags[piece.color + '_long'] = False

def _castlingCondition(gameState, piece, coord, new_coord)
    #TODO dopisać warunki na szach po drodze itd
    return gameState.castling_flags[piece.color + ("_long" if new_coord[0] < coord[0] else "_short")]

def _castlingConsequences(gameState, piece, coord, new_coord):
    making_move(board, ((coord[1], 0 if new_coord[0] < coord[0] else (GRID_SIZE-1)), (coord[1], (coord[0]-new_coord[0])//2)))
    _kingMoveConsequence(gameState, piece, coord, new_coord)


class Rook(Piece):
    tag = 'R'

    def __init__(self, color):
        self.color = color
        self.movement = list(map(lambda it: (it, True, None, _rookMoveConsequence), rotations(N)))

def _rookMoveConsequence(gameState, piece, coord, new_coord):
    gameState.castling_flags[piece.color + ('_long' if coord[0]==0 else '_short')] = False


class Knight(Piece):
    tag = 'N'

    def __init__(self, color):
        self.color = color
        self.movement = list(map(lambda it: (it, False, None, None), rotations(NNE) + rotations(NNW)))


class Bishop(Piece):
    tag = 'B'

    def __init__(self, color):
        self.color = color
        self.movement = list(map(lambda it: (it, True, None, None), rotations(NE)))


class Queen(Piece):
    tag = 'Q'

    def __init__(self, color):
        self.color = color
        self.movement = list(map(lambda it: (it, True, None, None), rotations(N) + rotations(NE)))
