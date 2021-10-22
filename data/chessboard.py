from data.constants import N, W, E, S, GRID_SIZE
from data.pieces import Pawn, Rook, Knight, Bishop, Queen, King
from data.functions import sum_directions, multiply_direction
from data.pieces import Pawn, Rook, Knight, Bishop, Queen, King


"""PRZECHOWUJE AKTUALNY STAN GRY"""
class GameState:
    def __init__(self, game_filepath="data/classic_new_game.csv"):
        with open(game_filepath, 'r') as file:
            self.nextMoveColor, *boardRowsText = file.read().split('\n')
        piecesClsDict = {pieceClass.tag: pieceClass for pieceClass in [Pawn, Rook, Knight, Bishop, Queen, King]}
        self.board = [[None if tag == '' else piecesClsDict[tag[1]](tag[0]) for tag in row.split(',')] for row in boardRowsText]
        self.castling_flags = {'w_long': True, 'w_short': True, 'b_long': True, 'b_short': True}
        self.en_passant_coord = None



    def making_move(self, shift):
        self.board[shift[1][1]][shift[1][0]] = self.board[shift[0][1]][shift[0][0]]
        self.board[shift[0][1]][shift[0][0]] = None

    def __str__(self):
        return '\n'.join([' '.join(map(lambda x: '  ' if x is None else str(x), boardRow)) for boardRow in self.board])
