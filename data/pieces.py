from .functions import rotations, multiply_direction, sum_directions
from .constants import *

class Piece:
    color = None
    tag = None

    def __init__(self, coord):
        self.coord = coord

    def __str__(self):
        return self.color + self.tag

    def get_full_name(self):
        return '_'.join(['black' if self.color == 'b' else 'white', type(self).__name__.lower()])

class Pawn(Piece):
    tag = 'P'

    def __init__(self, color, coord):
        super().__init__(coord)
        self.color = color
        self.direction = N if color == 'w' else S
        self.movement = list(map(lambda it: (it, False, _pawnDiagonalCondition, _pawnDiagonalConsequence),
                                 [(1, self.direction[1]), (-1, self.direction[1])]))
        self.movement.append((self.direction, False, _pawnForwardCondition, _pawnForwardConsequence))
        self.movement.append(
            (multiply_direction(self.direction, 2), False, _pawnDoubleForwardCondition, _pawnDoubleForwardConsequence))



    # PROTOTYP
    def attacked_fields(self, coord):
        attacked_field_list = []
        direction = N if self.color == 'w' else S
        diagonal_moves = (1, direction[1]), (-1, direction[1])
        for move in diagonal_moves:
            new_coord = sum_directions(move, coord)
            if min(new_coord) >= 0 and max(new_coord) < GRID_SIZE:
                attacked_field_list.append(new_coord)
        return attacked_field_list

def _pawnDiagonalCondition(gameState, piece, coord, new_coord):
    return (gameState.board[new_coord[1]][new_coord[0]] is not None and gameState.board[new_coord[1]][
        new_coord[0]].color != piece.color) or gameState.en_passant_coord == new_coord


def _pawnDiagonalConsequence(gameState, piece, coord, new_coord):
    if gameState.en_passant_coord == new_coord:
        gameState.board[coord[1]][new_coord[0]] = None
    _pawnForwardConsequence(gameState, piece, coord, new_coord)


def _pawnForwardCondition(gameState, piece, coord, new_coord):
    return gameState.board[new_coord[1]][new_coord[0]] is None


def _pawnForwardConsequence(gameState, piece, coord, new_coord):
    if new_coord[1] == (0 if piece.color == 'w' else GRID_SIZE - 1):
        gameState.board[new_coord[1]][new_coord[0]] = pawn_promotion(player_color=piece.color)


def _pawnDoubleForwardCondition(gameState, piece, coord, new_coord):
    return gameState.board[new_coord[1]][new_coord[0]] is None and gameState.board[(new_coord[1] + coord[1]) // 2][
        new_coord[0]] is None and coord[1] == (6 if piece.color == 'w' else 1)


def _pawnDoubleForwardConsequence(gameState, piece, coord, new_coord):
    gameState.new_en_passant_coord = (new_coord[0], (new_coord[1] + coord[1]) // 2)

def pawn_promotion(player_color):
    pieces_to_promotion = {'R': Rook, 'N': Knight, 'B': Bishop, 'Q': Queen}
    while True:
        picked_tag = input('Wybierz tag figury: Q, N, R, B').upper()
        if picked_tag in pieces_to_promotion:
            print(pieces_to_promotion[picked_tag](player_color))
            return pieces_to_promotion[picked_tag](player_color)

class King(Piece):
    tag = 'K'

    def __init__(self, color, coord):
        super().__init__(coord)
        self.color = color
        self.movement = list(map(lambda it: (it, False, None, _kingMoveConsequence), rotations(N) + rotations(NE)))
        self.movement.append((WW, False, _castlingCondition, _castlingConsequence))
        self.movement.append((EE, False, _castlingCondition, _castlingConsequence))


def _kingMoveConsequence(gameState, piece, coord, new_coord):
    gameState.castling_flags[piece.color + '_short'] = False
    gameState.castling_flags[piece.color + '_long'] = False


def _castlingCondition(gameState, piece, coord, new_coord):
    neededEmpty = [(column, coord[1]) for column in
                   (range(1, coord[0]) if new_coord[0] < coord[0] else range(coord[0] + 1, GRID_SIZE - 1))]
    neededUnAttacked = [coord, new_coord, ((coord[0] + new_coord[0]) // 2, coord[1])]
    return gameState.castling_flags[piece.color + ("_long" if new_coord[0] < coord[0] else "_short")] \
           and not any(map((lambda x: gameState.board[x[1]][x[0]]), neededEmpty))
    # and all([gameState.board[tmpCoord[1]][tmpCoord[0]] is None for tmpCoord in neededEmpty])
    # all(list(map(not isTileAttacked(gameState, tmpCoord), needenUnAttacked)))


def _castlingConsequence(gameState, piece, coord, new_coord):
    gameState.making_move(
        ((0 if new_coord[0] < coord[0] else (GRID_SIZE - 1), coord[1]), (((coord[0] + new_coord[0]) // 2), coord[1])))
    _kingMoveConsequence(gameState, piece, coord, new_coord)


class Rook(Piece):
    tag = 'R'

    def __init__(self, color, coord):
        super().__init__(coord)
        self.color = color
        self.movement = list(map(lambda it: (it, True, None, _rookMoveConsequence), rotations(N)))

def _rookMoveConsequence(gameState, piece, coord, new_coord):
    gameState.castling_flags[piece.color + ('_long' if coord[0] == 0 else '_short')] = False


class Knight(Piece):
    tag = 'N'

    def __init__(self, color, coord):
        super().__init__(coord)
        self.color = color
        self.movement = list(map(lambda it: (it, False, None, None), rotations(NNE) + rotations(NNW)))


class Bishop(Piece):
    tag = 'B'

    def __init__(self, color, coord):
        super().__init__(coord)
        self.color = color
        self.movement = list(map(lambda it: (it, True, None, None), rotations(NE)))


class Queen(Piece):
    tag = 'Q'

    def __init__(self, color, coord):
        super().__init__(coord)
        self.color = color
        self.movement = list(map(lambda it: (it, True, None, None), rotations(N) + rotations(NE)))
