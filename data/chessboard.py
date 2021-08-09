from Szachy.data.constants import N, W, E, S
from Szachy.data.pieces import Pawn, Rook, Knight, Bishop, Queen, King
from Szachy.data.game_logic import sum_directions, multiply_direction

class GameState:
    def __init__ (self, gameFilePath="data/classic_new_game.csv"):
        with open(gameFilePath,'r') as f:
            self.nextMoveColor, *pieceRowsText = f.read().split('\n')
        pieceClassesDict = {pieceClass.tag: pieceClass for pieceClass in [Pawn, Rook, Knight, Bishop, Queen, King]}
        self.board = [[None if pieceKey is '' else pieceClassesDict[pieceKey[1]](pieceKey[0]) for pieceKey in pieceRowText.split(',')] for pieceRowText in pieceRowsText]




    def generating_all_moves_for_piece(self, board, piece, coord):
        # PAWN MOVES
        moves_list = []
        if piece.tag == "P":
            pawn_movement = piece.movement
            new_coord = sum_directions(coord, pawn_movement)
            if board[new_coord[1]][new_coord[0]] is None:
                moves_list.append(list(pawn_movement))
                new_coord = sum_directions(coord, pawn_movement, pawn_movement)
                if coord[1] == (6 if piece.color == 'w' else 1) and board[new_coord[1]][new_coord[0]] is None:
                    moves_list.append(list(sum_directions(pawn_movement, pawn_movement)))
            for horizontal_shift in [W,E]:
                new_coord = sum_directions(coord, (sum_directions(pawn_movement, horizontal_shift)))
                if board[new_coord[1]][new_coord[0]] is not None and board[new_coord[1]][new_coord[0]].color != piece.color:
                    moves_list.append(list(sum_directions(pawn_movement, horizontal_shift)))

        # MOVES OF OTHER PIECES
        else:
            for j in range(len(piece.movement)):
                for i in range(piece.movement_range):
                    increased_piece_movement = multiply_direction(piece.movement[j], i + 1)
                    # i jest mnoznikiem odleglosci
                    coords_after_move = sum_directions(coord, increased_piece_movement)
                    # if pilnujacy zeby generowane ruchy nie wychodzilo poza zakres planszy
                    if min(coords_after_move) >= 0 and max(coords_after_move) < 8:
                        if board[coords_after_move[1]][coords_after_move[0]] is not None:
                            # jezeli napotka na przeszkode przerywa iteracje po dlugosci ruchu
                            if board[coords_after_move[1]][coords_after_move[0]].color == piece.color:
                                break
                            else:
                                moves_list.append(increased_piece_movement)
                                break
                        else:
                            moves_list.append(increased_piece_movement)

        if len(moves_list) == 0:
            return None
        return moves_list


    def __str__(self):
        return '\n'.join([' '.join(map(lambda x:'  ' if x is None else str(x),boardRow)) for boardRow in self.board])


