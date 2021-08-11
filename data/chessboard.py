from data.constants import N, W, E, S
from data.pieces import Pawn, Rook, Knight, Bishop, Queen, King
from data.game_logic import sum_directions, multiply_direction, sub_directions


class GameState:
    """PRZECHOWUJE AKTUALNY STAN GRY"""

    def __init__(self, game_filepath="data/classic_new_game.csv"):
        with open(game_filepath, 'r') as file:
            self.nextMoveColor, *boardRowsText = file.read().split('\n')
        #  LISTA KLAS-FIGUR DO INICJALIZACJI
        piecesClsDict = {pieceClass.tag: pieceClass for pieceClass in [Pawn, Rook, Knight, Bishop, Queen, King]}
        #  POLE GRY
        self.board = [[None if tag == '' else piecesClsDict[tag[1]](tag[0])  # pieces_ClsDict[]() == Piece(color)
                       for tag in row.split(',')]
                      for row in boardRowsText]
        self.castling_flags = {'w_long': True, 'w_short': True, 'b_long': True, 'b_short': True}

    def _castling(self, coord, color):
        castling_move = []
        if self.castling_flags[color+'_short'] is True:  # SHORT
            castling_move.extend((sum_directions(coord, (-2, 0)),
                                  (sum_directions(coord, (-4, 0)), sum_directions(coord, (-1, 0)))))
        if self.castling_flags[color+'_long'] is True:  # LONG
            castling_move.extend((sum_directions(coord, (2, 0)),
                                  (sum_directions(coord, (3, 0)), sum_directions(coord, (1, 0)))))
        return castling_move


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
                # FIXME BUG sprawdzane wspolrzedne wychodza poza game.board
                if board[new_coord[1]][new_coord[0]] is not None and \
                        board[new_coord[1]][new_coord[0]].color != piece.color:
                    # moves_list.append(list(sum_directions(pawn_movement, horizontal_shift)))
                    moves_list.append(tuple(new_coord))
            #  MOVES OF OTHER PIECES
        else:
            if piece.tag =='K':
                moves_list.extend(self._castling(coord, piece.color))
            for singleMove in piece.movement:
                for multiplier in range(piece.movement_range):
                    increased_piece_movement = multiply_direction(singleMove, multiplier + 1)
                    coords_after_move = sum_directions(coord, increased_piece_movement)
                    # if pilnujacy zeby generowane ruchy nie wychodzilo poza zakres planszy
                    if min(coords_after_move) >= 0 and max(coords_after_move) < 8:
                        if board[coords_after_move[1]][coords_after_move[0]] is not None:
                            # jezeli napotka na przeszkode przerywa iteracje po dlugosci ruchu
                            if board[coords_after_move[1]][coords_after_move[0]].color == piece.color:
                                break
                            else:
                                moves_list.append(coords_after_move)
                                break
                        else:
                            moves_list.append(coords_after_move)
            if not len(moves_list) == 0:
                return moves_list
            else:
                #  TODO - ustalic czy ma zwracac [] czy None
                return None

    def __str__(self):
        return '\n'.join([' '.join(map(lambda x: '  ' if x is None else str(x), boardRow)) for boardRow in self.board])
