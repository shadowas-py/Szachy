from Szachy.data.constants import N, W, E, S
from Szachy.data.pieces import Pawn, Rook, Knight, Bishop, Queen, King
from Szachy.data.game_logic import sum_directions, multiply_direction

class GameState:
    def __init__ (self, gameFilePath="data/classic_new_game.csv"):
        with open(gameFilePath,'r') as f:
            self.nextMoveColor, *pieceRowsText = f.read().split('\n')
        pieceClassesDict = {pieceClass.tag: pieceClass for pieceClass in [Pawn, Rook, Knight, Bishop, Queen, King]}
        self.board = [[None if pieceKey is '' else pieceClassesDict[pieceKey[1]](pieceKey[0]) for pieceKey in pieceRowText.split(',')] for pieceRowText in pieceRowsText]




    def generating_all_moves_for_piece(self, board, piece, coord):  # WYPISYWANIE KOLEJNYCH KOLUMN
        # PAWN MOVES
        moves_list = []
        if piece.__class__.__name__ == "Pawn":
            if piece.color == 'w':
                pawn_starting_row = 6
                pawn_direction = N
                opponent_color = 'b'
            else:
                pawn_starting_row = 1
                pawn_direction = S
                opponent_color = 'w'


            moves_list = []
            new_coord = sum_directions(coord, pawn_direction)
            if board[new_coord[1]][new_coord[0]] is None:
                moves_list.append(list(pawn_direction))
                new_coord = sum_directions(coord, (sum_directions(pawn_direction, pawn_direction)))
                if coord[1] == pawn_starting_row and board[new_coord[1]][new_coord[0]] is None:  # Jezeli pionek znajduje sie w rzedzie startowym
                    moves_list.append(list(sum_directions(pawn_direction, pawn_direction)))
            new_coord = sum_directions(coord, (sum_directions(pawn_direction, W)))
            if board[new_coord[1]][new_coord[0]] is not None and board[new_coord[1]][new_coord[0]].color == opponent_color:
                moves_list.append(list(sum_directions(pawn_direction, W)))
            new_coord = sum_directions(coord, (sum_directions(pawn_direction, E)))
            if board[new_coord[1]][new_coord[0]] is not None and board[new_coord[1]][new_coord[0]].color == opponent_color:
                moves_list.append(list(sum_directions(pawn_direction, E)))
            if len(moves_list) == 0:
                moves_list = None
                return moves_list
            else:
                return moves_list


        # REST MOVES
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
            if not len(moves_list) == 0:
                return moves_list
            else:
                return None


    def __str__(self):
        return '\n'.join([' '.join(map(lambda x:'  ' if x is None else str(x),boardRow)) for boardRow in self.board])


