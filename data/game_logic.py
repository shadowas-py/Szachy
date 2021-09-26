import pygame

from .constants import BOARD_POSITION, TILE_SIZE, BOARD_END_POSITION
from .functions import midpoint_between_two_coords
from .pieces import Rook, Knight, Bishop, Queen


def get_game_coord_from_mouse():
    mouse_pos = pygame.mouse.get_pos()
    coord = ((mouse_pos[0] - BOARD_POSITION[1]) // TILE_SIZE, (mouse_pos[1] - BOARD_POSITION[0]) // TILE_SIZE)
    if BOARD_END_POSITION >= mouse_pos >= BOARD_POSITION:
        return coord
    else:
        return None


def selecting_piece(board, coord, active_player):
    row, col = coord
    piece = board[col][row]
    if piece is not None and piece.color == active_player:
        return piece
    return None


def making_move(board, moves_list):
    for shift in moves_list:
        piece = board[shift[0][1]][shift[0][0]]
        board[shift[0][1]][shift[0][0]] = None
        board[shift[1][1]][shift[1][0]] = piece


# ZAKLADAM ZE RUCH ZOSTAL WYKONANY
def disabling_castling_flags(game, piece, base_coord):
    if piece.tag == 'K':
        game.castling_flags[piece.color + '_short'] = False
        game.castling_flags[piece.color + '_long'] = False
    elif piece.tag == 'R':
        if base_coord == (0, 0):
            game.castling_flags[piece.color + '_long'] = False
        if base_coord == (0, 7):
            game.castling_flags[piece.color + '_long'] = False
        if base_coord == (7, 0):
            game.castling_flags[piece.color + '_short'] = False
        if base_coord == (7, 7):
            game.castling_flags[piece.color + '_short'] = False


def set_en_passant_tile(base_coord, target_coord):
    en_passant_tile = midpoint_between_two_coords(base_coord, target_coord)
    return en_passant_tile


pieces_to_promotion = {'R': Rook, 'N': Knight, 'B': Bishop, 'Q': Queen}


def pawn_promotion(player_color):
    while True:
        picked_tag = input('Wybierz tag figury: Q, N, R, B').upper()
        if picked_tag in pieces_to_promotion:
            print(pieces_to_promotion[picked_tag](player_color))
            return pieces_to_promotion[picked_tag](player_color)


def switching_turns(active_player):
    return 'b' if active_player == 'w' else 'w'
