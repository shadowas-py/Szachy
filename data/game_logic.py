import pygame

from .constants import BOARD_POSITION, TILE_SIZE, BOARD_END_POSITION

'''moze uzyc numpy'''


def sum_directions(direction1, direction2, direction3=(0, 0)):
    return tuple(map(sum, zip(direction1, direction2, direction3)))


def sub_directions(direction1, direction2, ):
    return tuple(direction1 - direction2 for direction1, direction2 in zip(direction1, direction2))


def multiply_direction(direction, multiplier):
    multiplied_direction = (direction[0] * multiplier, direction[1] * multiplier)
    return list(multiplied_direction)


def get_game_coord_from_mouse():
    mouse_pos = pygame.mouse.get_pos()
    coord = ((mouse_pos[0] - BOARD_POSITION[1]) // TILE_SIZE, (mouse_pos[1] - BOARD_POSITION[0]) // TILE_SIZE)
    if BOARD_END_POSITION >= mouse_pos >= BOARD_POSITION:
        return coord
    else:
        return None


def selecting_piece(board, coord,
                    active_player):  # Zwraca None jeżeli nie jest klikniete pole z figura aktywnego gracza
    row, col = coord
    piece = board[col][row]
    if piece is not None:  # obiekt nie moze byc None
        if piece.color == active_player:
            return piece
        return None


# zeby nie wywalalo jak kliknie sie poza plansze
def making_move(board, moves_list):
    for shift in moves_list:
        piece = board[shift][0]
        board[shift][0] = None
        board[shift][1] = piece


def switching_turns(active_player):
    if active_player == "w":
        return 'b'
    else:
        return "w"

# class SpecialMoves:
#     def __init__(self):
#         self.w_long_castling_flag = True
#         self.w_short_castling_flag = True
#         self.b_long_castling_flag = True
#         self.b_short_castling_flag = True
#         en_passant_flag = False
#
#     def castling(self):
#         short_castling = sum_directions(E, E)
#         long_castling = sum_directions(W, W)
#         if self.w_long_castling_flag:
#             if self.w_short_castling_flag:
#                 return short_castling, long_castling
#         else:
#             if self.w_short_castling_flag :
#                 return short_castling
#
#     def en_passant():
#         pass

