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

def looking_for_pins(game, multiplier, singleMove, player, occupied_tile, base_coord):
    # print(base_coord,'base coord', 'IN FUNCTION ______________')
    # print(occupied_tile,'occupied tile')
    for _multiplier in range(multiplier+1, GRID_SIZE):
        new_coord = sum_directions(base_coord, multiply_direction(singleMove, _multiplier))
        # print(new_coord, 'NEW_COORD')
        if max(new_coord)>7 or min(new_coord)<0:
            # print('BREAK out of range')
            break
        targetPiece = game.board[new_coord[1]][new_coord[0]]
        if targetPiece is None:
            continue
        elif targetPiece.tag == 'K' and targetPiece.color != player.color :
            print('setting absolute pins', new_coord, occupied_tile)
            player.absolute_pins[occupied_tile]=base_coord
        else:
            # print('BREAK')
            break





def looking_for_absolute_pins(game, piece, coord, player):
    moves_list = {}
    base_coord = coord
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
                    looking_for_pins(game, multiplier, singleMove,
                                     player, occupied_tile=new_coord, base_coord=base_coord)
                    if targetPiece.color != piece.color:
                        moves_list[new_coord] = consequenceFunc
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


def switching_turns(active_player, **players):
    return players['player1'] if active_player == players['player2'] else players['player2']
