from data.constants import N, W, E, S, GRID_SIZE
from data.pieces import Pawn, Rook, Knight, Bishop, Queen, King
from data.functions import sum_directions, multiply_direction


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
        self.en_passant_coord = None

    def _castling(self, coord, color):
        castling_move = []
        if self.castling_flags[color+'_short'] is True:  # SHORT
            castling_move.extend((sum_directions(coord, (-2, 0)),
                                  (sum_directions(coord, (-4, 0)), sum_directions(coord, (-1, 0)))))
        if self.castling_flags[color+'_long'] is True:  # LONG
            castling_move.extend((sum_directions(coord, (2, 0)),
                                  (sum_directions(coord, (3, 0)), sum_directions(coord, (1, 0)))))
        return castling_move

    def generating_all_moves_for_piece(self, game, piece, coord):
        # PAWN MOVES
        moves_list = []
        if piece.tag == 'K':
            moves_list.extend(self._castling(coord, piece.color))
        for singleMove in piece.movement:
            for multiplier in range(1, piece.movement_range+1):
                coords_after_move = sum_directions(coord, multiply_direction(singleMove, multiplier))
                
                if piece.tag == "P":
                    if game.board[coords_after_move[1]][coords_after_move[0]] is None:
                        moves_list.append(tuple(coords_after_move))
                        new_coord = sum_directions(coord, singleMove, singleMove)
                        if coord[1] == (6 if piece.color == 'w' else 1) and game.board[new_coord[1]][new_coord[0]] is None:
                            moves_list.append(tuple(new_coord))
                    for horizontal_shift in [W, E]:
                        new_coord = sum_directions(coord, (sum_directions(singleMove, horizontal_shift)))
                        if game.en_passant_coord == new_coord:
                            moves_list.append(game.en_passant_coord)
                            moves_list.append((coord, sum_directions(horizontal_shift, coord)))
                        if new_coord[0] >= 0 and new_coord[0] < GRID_SIZE and\
                                game.board[new_coord[1]][new_coord[0]] is not None and \
                                game.board[new_coord[1]][new_coord[0]].color != piece.color:
                            moves_list.append(tuple(new_coord))
                            
                else:
                    if min(coords_after_move) >= 0 and max(coords_after_move) < GRID_SIZE:
                        if game.board[coords_after_move[1]][coords_after_move[0]] is not None:
                            if game.board[coords_after_move[1]][coords_after_move[0]].color != piece.color:
                                moves_list.append(coords_after_move)
                            break
                        else:
                            moves_list.append(coords_after_move)
        if len(moves_list) == 0:
            return None
        return moves_list

    def __str__(self):
        return '\n'.join([' '.join(map(lambda x: '  ' if x is None else str(x), boardRow)) for boardRow in self.board])
