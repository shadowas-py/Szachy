from .constants import N, S, W, E

WHITE_PAWN_STARTING_ROW = 6
BLACK_PAWN_STARTING_ROW = 1


def sum_directions(direction1, direction2):
    return tuple(map(sum, zip(direction1, direction2)))


class Piece(object):
    def __init__(self, piece_selected, piece_coord):
        self.piece = piece_selected[1]
        self.piece_color = piece_selected[0]
        self.piece_coord = piece_coord


class Pawn(Piece):
    def __init__(self, board, piece_selected, piece_coord):  ### ///////////////////////////////////
        super().__init__(piece_selected, piece_coord)
        self.board = board

        def listing_pawn_moves_list():
            if self.piece_color == 'w':
                pawn_moves = [N]
                if self.piece_coord[1] == WHITE_PAWN_STARTING_ROW:  # Jezeli pionek znajduje sie w rzedzie startowym
                    pawn_moves.extend(sum_directions(N, N))
                if self.board(sum_directions(self.board.coord, (sum_directions(N, W)))) == 'b':
                    pawn_moves.extend(sum_directions(N, W))
                if self.board(sum_directions(self.board.coord, (sum_directions(N, E)))) == 'b':
                    pawn_moves.extend(sum_directions(N, E))
                return pawn_moves
            elif self.piece_color == 'b':
                pawn_moves = [S]
                if self.piece_coord[1] == BLACK_PAWN_STARTING_ROW:  # Jezeli pionek znajduje sie w rzedzie startowym
                    pawn_moves.extend(sum_directions(S, S))
                if self.board(sum_directions(self.board.coord, (sum_directions(S, W)))) == 'b':
                    pawn_moves.extend(sum_directions(S, W))
                if self.board(sum_directions(self.board.coord, (sum_directions(S, E)))) == 'b':
                    pawn_moves.extend(sum_directions(S, E))
                return pawn_moves

        self.moves_list = listing_pawn_moves_list(self)


# MOVEMENT ={
#     'wP': (UP, (0, -2)),
#     'wR': (UP, RIGHT, LEFT, DOWN),
#     'wB': UP,
#     'wN': UP,
#     'wQ': UP,
#     'wK': UP,
#     'bP': (DOWN, (0, 2)),
#     'bR': UP,
#     'bN': UP,
#     'bB': UP,
#     'bQ': UP,
#     'bK': UP,
# }
#
# ONLY_CAPTURING_MOVEMENT = {
#     'wP':(UP+LEFT,UP+RIGHT),
#     'bP':(DOWN+LEFT, DOWN+RIGHT)
# }

# class Piece:
#     def __init__(self):
#         pass

# def valid_pawn_moves(piece_selected, piece_coord, target_content, target_coord):  # move
#     moves_allowed = []  # TU
#     if piece_selected[0] == "w":  # JEZELI JEST BIALY
#         if piece_coord[1] < 6:  # JEZELI NIE JEST TO JEGO PIERWSZY RUCH
#             if target_content[0] == '-':  # JEZELI POLE DOCELOWE JEST PUSTE
#                 moves_allowed = MOVEMENT['wP']
#                 return moves_allowed
#             else:  # JEZELI POLE DOCELOWE JEST ZAJETE
#                 moves_allowed = ONLY_CAPTURING_MOVEMENT['wP']
#                 return moves_allowed
#         elif piece_coord[1] == 6:  # JEZELI JEST TO PIERWSZY RUCH TEJ BIERKI
#             if target_content[0] == '-':
#                 print(MOVEMENT['wP'])
#                 moves_allowed = tuple(MOVEMENT['wP'])
#                 return moves_allowed
#             else:
#                 moves_allowed = ONLY_CAPTURING_MOVEMENT['wP']
#                 return moves_allowed
#         elif target_coord[1] == 0:
#             if target_content[0] != '-':
#                 moves_allowed = MOVEMENT['wP']
#                 return moves_allowed  # promocja
#             else:
#                 moves_allowed = ONLY_CAPTURING_MOVEMENT['wP']  # promocja
#                 return moves_allowed
#     elif piece_selected[0] is "b":  # JEZELI CZARNY
#         if piece_coord[1] > 1:  # JEZELI NIE JEST TO JEGO PIERWSZY RUCH
#             if target_content[0] == '--':  # JEZELI POLE DOCELOWE JEST PUSTE
#                 moves_allowed = MOVEMENT['bP']
#                 return moves_allowed
#             else:  # JEZELI POLE DOCELOWE JEST ZAJETE
#                 moves_allowed = ONLY_CAPTURING_MOVEMENT['bP']
#                 return moves_allowed
#         elif piece_coord[1] == 1:  # JEZELI JEST TO PIERWSZY RUCH TEJ BIERKI
#             if target_content[0] == '-':
#                 moves_allowed = (MOVEMENT['bP'])
#                 return moves_allowed
#             else:
#                 moves_allowed = ONLY_CAPTURING_MOVEMENT['bP']
#                 return moves_allowed
#         elif target_coord[1] == 7:
#             if target_content[0] != '-':
#                 moves_allowed = MOVEMENT['bP']
#                 return moves_allowed  # promocja
#             else:
#                 moves_allowed = ONLY_CAPTURING_MOVEMENT['bP']  # promocja
#                 return moves_allowed
#         pass

        # self.wK = (DIRECTIONS.values())
            # castling = (2,0)(1,0)

        
        # if piece = king
        #     long_castling_flag = False
        #     short_castling_flag = False

        #     long_castling_flag = True
        #     short_castling_flag = True

        #     def castling ():
        #         if move == (2,0):
        #             board(7,7) = '--'
        #             board(6,7) = self.king()
        #             board(5,7) = self.rook()
        #             rook = (king.coord[0]-1)
        #         else:
        #             board(0,7) = '--'
        #             board(2,7) = self.king()

        # self.knight_moves():
        #     if abs(move)==3 
        #         pass
        #     else:
        #         pass
        #     # moves_list (1,2) (-1,2) (1,-2)(-1,-2) (-2, 1)(-2,-1) (2, 1) (2, -1)
        # self.bishop()# NIEDOROBIONE
        #     if sum(coord) % 2 != 0 :
        #         if move [row] == move [col] or sum(move) == sum(coord)
        #         return moves_allowed
        #     else:
        #         if move [row] == move [col] or sum(move) == sum(coord)
            
        # self.rook ()
        #     if (abs(0,move[1])) or (abs(move[0],0)):
        #         pass 
        # self.queen()
        #     self.rook()
        #     self.bishop()
        # self.king()
        #     self.queen
        # pass
