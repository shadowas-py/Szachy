import pygame

from .constants import BOARD_POSITION, TILE_SIZE, BOARD_END_POSITION, GRID_SIZE
from .functions import sum_directions, multiply_direction


def get_game_coord_from_mouse():
    mouse_pos = pygame.mouse.get_pos()
    coord = ((mouse_pos[0] - BOARD_POSITION[1])//TILE_SIZE, (mouse_pos[1] - BOARD_POSITION[0])//TILE_SIZE)
    if max(BOARD_POSITION) <= min(mouse_pos) and max(mouse_pos) <= min(BOARD_END_POSITION):
        return coord
    else:
        return None


def selecting_piece(board, coord, active_player):
    row, col = coord
    piece = board[col][row]
    if piece is not None and piece.color == active_player:
        return piece
    return None

def looking_for_pins(game, coord, multiplier, singleMove, piece, base_coord):
    multiplier+=1
    for _multiplier in range(multiplier, GRID_SIZE):
        new_coord = sum_directions(coord, multiply_direction(singleMove, multiplier))
        targetPiece = game.board[new_coord[1]][new_coord[0]]
        if targetPiece.tag != 'K' and targetPiece.color != piece.color:
            break
        elif targetPiece.tag == 'K':
            player.pinned_figures[new_coord]=base_coord


def looking_for_absolute_pins(game, piece, coord):
    moves_list = {}
    pinned_fields = {}# {wspolrzedne zwiazanej figury: suma wspolrzednych wchodzacych w zakresie zwiazania}
    pinned_figure = {}# {coord zwiazanej figury: coord zwiazujacej}
    base_coord = coord
    blocked_by_piece = False
    for movePack in piece.movement:
        singleMove, scalable, conditionFunc, consequenceFunc = movePack
        for multiplier in range(1, GRID_SIZE if scalable else 2):
            new_coord = sum_directions(coord, multiply_direction(singleMove, multiplier))
            if min(new_coord) < 0 or max(new_coord) >= GRID_SIZE:
                break
            elif conditionFunc is None:
                targetPiece = game.board[new_coord[1]][new_coord[0]]
                if targetPiece is None:
                    moves_list[new_coord] = consequenceFunc
                else:
                    if targetPiece.color != piece.color:
                        moves_list[new_coord] = consequenceFunc
                    looking_for_pins(game, new_coord, multiplier, singleMove, piece, base_coord)
                    break
            elif conditionFunc(game, piece, coord, new_coord):
                moves_list[new_coord] = consequenceFunc
    return moves_list





def generating_all_moves_for_piece(game, piece, coord):
    moves_list = {}
    for movePack in piece.movement:
        singleMove, scalable, conditionFunc, consequenceFunc = movePack
        for multiplier in range(1, GRID_SIZE if scalable else 2):
            new_coord = sum_directions(coord, multiply_direction(singleMove, multiplier))
            if min(new_coord) < 0 or max(new_coord) >= GRID_SIZE:
                break
            elif conditionFunc is None:
                targetPiece = game.board[new_coord[1]][new_coord[0]]
                if targetPiece is None:
                    moves_list[new_coord] = consequenceFunc
                else:
                    if targetPiece.color != piece.color:
                        moves_list[new_coord] = consequenceFunc
                    break
            elif conditionFunc(game, piece, coord, new_coord):
                moves_list[new_coord] = consequenceFunc
    return moves_list


def switching_turns(active_player):
    return 'b' if active_player == 'w' else 'w'
