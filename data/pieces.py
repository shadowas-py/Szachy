from .constants import N, S, W, E, GRID_SIZE

def sum_directions(direction1, direction2, direction3=(0, 0)):
    return tuple(map(sum, zip(direction1, direction2, direction3)))

def listing_all_posible_moves_for_the_piece(piece_movement, movement_range, piece_coord):
    moves_list = []
    for i in range(movement_range):
        for j in range(len(piece_movement)):
            increased_piece_movement = sum_directions(piece_movement[j], (i, i))  # kierunek ruchu z mnoznikiem 'i'
            coords_after_move = sum_directions(piece_coord, increased_piece_movement)
            if min(coords_after_move) >= 0 and max(coords_after_move) < 18:
                moves_list.append(increased_piece_movement)
             # jak wyjde poza zakres planszy to zaczynam sprawdzac kolejne kierunki(piece_movement)
    return moves_list

class Pieces(object):
    def __init__(self, board, piece_coord, piece_selected):
        self.piece_color = piece_selected[0]
        self.piece_coord = piece_coord
        self.board = board

    def swap_piece_symbol_to_object(self, piece_selected):

        PIECE_OBJECTS = {'P': Pawn(self.board, self.piece_color, self.piece_coord),
                         'R': Rook(self.board, self.piece_color,self.piece_coord),
                         'N': Knight(self.board, self.piece_color,self.piece_coord),
                         'B': Bishop(self.board, self.piece_color,self.piece_coord),
                         'Q': Queen(self.board, self.piece_color,self.piece_coord),
                         'K': King(self.board, self.piece_color,self.piece_coord),
                         }
        return PIECE_OBJECTS[piece_selected[1]]


class Pawn():

    def __init__(self, board, piece_color, piece_coord):  ### ///////////////////////////////////
        self.movement_range = 1  # domyslna ilosc pól o jakie dana figura moze sie poruszac
        self.piece_color = piece_color
        self.piece_coord = piece_coord

        # Kolizje z innymi bierkami beda liczone gdzie indziej
        def listing_pawn_moves():
            if self.piece_color == 'w':
                white_pawn_starting_row = 6
                pawn_moves = N
                if self.piece_coord[1] == white_pawn_starting_row:  # Jezeli pionek znajduje sie w rzedzie startowym
                    pawn_moves.extend(sum_directions(N, N))
                new_coord = sum_directions(self.piece_coord, (sum_directions(N, W)))
                if board[new_coord[1]][new_coord[0]][0] == 'b':  # jeżeli czarny pion to moze bić w gore lewo
                    pawn_moves.extend(sum_directions(N, W))
                new_coord = sum_directions(self.piece_coord, (sum_directions(N, E)))
                if board[new_coord[1]][new_coord[0]][0] == 'b':  # jeżeli czarny pion to moze bić w gore prawo
                    pawn_moves.extend(sum_directions(N, E))
                return pawn_moves
            elif self.piece_color == 'b':  # to samo dla czarnego piona
                black_pawn_starting_row = 1
                pawn_moves = S
                if self.piece_coord[1] == black_pawn_starting_row:  # Jezeli pionek znajduje sie w rzedzie startowym
                    pawn_moves.extend(sum_directions(S, S))
                new_coord = sum_directions(self.piece_coord, (sum_directions(S, W)))
                if board[new_coord[1]][new_coord[0]][0] == 'w':
                    pawn_moves.extend(sum_directions(S, W))
                new_coord = sum_directions(self.piece_coord, (sum_directions(S, E)))
                if board[new_coord[1]][new_coord[0]][0] == 'w':
                    pawn_moves.extend(sum_directions(S, E))
                return pawn_moves

        self.all_moves = listing_pawn_moves()
        # TO DO
        # bicie w przelocie


class King():
    def __init__(self, board, piece_color, piece_coord): # parametry do poprawienia
        self.movement_range = 1
        self.movement = N, S, E, W, \
                          sum_directions(N, E), sum_directions(N, W), sum_directions(S, W), sum_directions(S, W)

        self.all_moves = listing_all_posible_moves_for_the_piece(self.movement, self.movement_range, piece_coord)
        # TO DO
        # dodac znaczniki i ruch roszady dla bialego i czarnego


class Rook():
    def __init__(self, board, piece_color, piece_coord):
        self.movement_range = GRID_SIZE
        self.movement = (N, S, E, W)
        self.all_moves = listing_all_posible_moves_for_the_piece(self.movement, self.movement_range, piece_coord)

class Knight():
    def __init__(self, board, piece_color, piece_coord):

        self.movement_range = GRID_SIZE
        self.movement = sum_directions(N, N, E), sum_directions(N, N, W), \
                          sum_directions(E, E, N), sum_directions(E, E, S), \
                          sum_directions(W, W, N), sum_directions(W, W, S), \
                          sum_directions(S, S, E), sum_directions(S, S, W)

        self.all_moves = listing_all_posible_moves_for_the_piece(self.movement, self.movement_range, piece_coord)

class Bishop():
    def __init__(self, board, piece_color, piece_coord):

        self.movement_range = GRID_SIZE
        self.movement = sum_directions(N, E), sum_directions(N, W), \
                          sum_directions(S, E), sum_directions(S, W), \

        self.all_moves = listing_all_posible_moves_for_the_piece(self.movement, self.movement_range, piece_coord)

class Queen():
    def __init__(self, board, piece_color, piece_coord):

        self.movement_range = GRID_SIZE
        self.movement = N, S, E, W, sum_directions(N, E), sum_directions(N, W), \
                          sum_directions(S, E), sum_directions(S, W), \

        self.all_moves = listing_all_posible_moves_for_the_piece(self.movement, self.movement_range, piece_coord)

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
