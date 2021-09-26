from data.constants import N, W, E, S, GRID_SIZE
from data.pieces import Pawn, Rook, Knight, Bishop, Queen, King
from data.functions import sum_directions, multiply_direction


"""PRZECHOWUJE AKTUALNY STAN GRY"""
class GameState:
    def __init__(self, game_filepath="data/classic_new_game.csv"):
        with open(game_filepath, 'r') as file:
            self.nextMoveColor, *boardRowsText = file.read().split('\n')
        piecesClsDict = {pieceClass.tag: pieceClass for pieceClass in [Pawn, Rook, Knight, Bishop, Queen, King]}
        self.board = [[None if tag == '' else piecesClsDict[tag[1]](tag[0]) for tag in row.split(',')] for row in boardRowsText]
        self.castling_flags = {'w_long': True, 'w_short': True, 'b_long': True, 'b_short': True}
        self.en_passant_coord = None

    def generating_all_moves_for_piece(self, game, piece, coord):
        moves_list = []
        for movePack in piece.movement:
            singleMove, scalable, conditionFunc, consequencesFunc = movePack
            for multiplier in range(1, GRID_SIZE if scalable else 1):
                new_coord = sum_directions(coord, multiply_direction(singleMove, multiplier))
                if min(coords_after_move) < 0 or max(coords_after_move) >= GRID_SIZE:
                    break
                elif conditionFunc is None or conditionFunc(self.board, piece, coord, new_coord):
                    moves_list.append(new_coord, consequencesFunc)
        return moves_list

    def __str__(self):
        return '\n'.join([' '.join(map(lambda x: '  ' if x is None else str(x), boardRow)) for boardRow in self.board])
