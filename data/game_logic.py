import pygame

from .constants import BOARD_POSITION, TILE_SIZE, BOARD_END_POSITION
from .functions import sum_directions, multiply_direction
from .pieces import Pawn, Rook, Knight, Bishop, Queen, King


def get_game_coord_from_mouse():
    mouse_pos = pygame.mouse.get_pos()
    coord = ((mouse_pos[0] - BOARD_POSITION[1])//TILE_SIZE, (mouse_pos[1] - BOARD_POSITION[0])//TILE_SIZE)
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

def making_move(board, shift):
    board[shift[1][1]][shift[1][0]] = board[shift[0][1]][shift[0][0]]
    board[shift[0][1]][shift[0][0]] = None



pieces_to_promotion = {'R': Rook, 'N': Knight, 'B': Bishop, 'Q': Queen}
def pawn_promotion(player_color):
    while True:
        picked_tag = input('Wybierz tag figury: Q, N, R, B').upper()
        if picked_tag in pieces_to_promotion:
            print(pieces_to_promotion[picked_tag](player_color))
            return pieces_to_promotion[picked_tag](player_color)

def generating_all_moves_for_piece(game, piece, coord):
    moves_list = {}
    for movePack in piece.movement:
        singleMove, scalable, conditionFunc, consequenceFunc = movePack
        for multiplier in range(1, GRID_SIZE if scalable else 1):
            new_coord = sum_directions(coord, multiply_direction(singleMove, multiplier))
            if min(coords_after_move) < 0 or max(coords_after_move) >= GRID_SIZE:
                break
            elif conditionFunc is None or conditionFunc(game, piece, coord, new_coord):
                moves_list[new_coord] = consequenceFunc
    return moves_list

def switching_turns(active_player):
    return 'b' if active_player == 'w' else 'w'
