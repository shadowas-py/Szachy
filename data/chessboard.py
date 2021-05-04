from .pieces import Pawn, Rook, Knight, Bishop, Queen, King
from .game_logic import sum_directions, multiply_direction

class GameState:
    def __init__ (self, gameFilePath="classic_new_game.csv"):
        with open(gameFilePath,'r') as f:
            self.nextMoveColor, *boardRowsText = f.read().split('\n')
        pieceClassesDict = {pieceClass.tag: pieceClass for pieceClass in [Pawn, Rook, Knight, Bishop, Queen, King]}
        self.board = [[None if pieceKey is '' else pieceClassesDict[pieceKey[1]](pieceKey[0]) for pieceKey in pieceRowText.split(',')] for pieceRowText in pieceRowsText]



    def generating_all_moves_for_piece(self, board, piece, coord,):  # WYPISYWANIE KOLEJNYCH KOLUMN
        moves_list = []
        for j in range(len(piece.movement)):
            for i in range(piece.movement_range):
                increased_piece_movement = multiply_direction(piece.movement[j], i + 1) # i jest mnoznikiem odleglosci
                coords_after_move = sum_directions(coord, increased_piece_movement)
                col, row = coords_after_move
                # if pilnujacy zeby generowane ruchy nie wychodzilo poza zakres planszy
                if min(coords_after_move) >= 0 and max(coords_after_move) < 8:
                    if board[row][col] != None: # jezeli napotka na przeszkode przerywa iteracje po dlugosci ruchu
                        if board[row][col].color == piece.color:
                            break
                        else:
                            moves_list.append(increased_piece_movement)
                            break
                    else:
                        moves_list.append(increased_piece_movement)

        if not len(moves_list) == 0:
            return moves_list
        else:
            return None


    def __str__(self):
        return '\n'.join([' '.join(map(lambda x:'  ' if x is None else str(x),boardRow)) for boardRow in self.board])


