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
            player.absolute_pins[occupied_tile]=base_coord
            break
        else:
            # print('BREAK')
            break


def looking_for_absolute_pins(game, piece, coord, player): # amd attacked tiles
    attacked_tiles = set()
    base_coord = coord
    if piece.tag == 'P':
        for i in piece.attacked_fields(coord):
            # print('SET', coord, piece, i)
            attacked_tiles.update([i])
    for movePack in piece.movement:
        # print(coord, piece, player.color)
        singleMove, scalable, conditionFunc, consequenceFunc = movePack
        for multiplier in range(1, GRID_SIZE if scalable else 2):
            new_coord = sum_directions(coord, multiply_direction(singleMove, multiplier))
            if min(new_coord) < 0 or max(new_coord) >= GRID_SIZE:
                # print('BREAK out of range',new_coord,)
                break
            elif conditionFunc is None:
                targetPiece = game.board[new_coord[0]][new_coord[1]]
                if targetPiece is None:
                    ...
                    # attacked_tiles.update([new_coord])
                else:
                    looking_for_pins(game, multiplier, singleMove,
                                     player, occupied_tile=new_coord, base_coord=base_coord)
                    if targetPiece.color != piece.color:
                        ...
                        # print('SET coord:',new_coord, targetPiece,piece )
                        # attacked_tiles.update([new_coord])
                        # print('in', moves_list)
                    else:
                        # print('BREAK same_color', new_coord,targetPiece, 'NEW COORD',piece )
                        break
            elif conditionFunc(game, piece, coord, new_coord):
                # print('PASS coord:condition_func',new_coord)
                pass
    # print(moves_list.keys(),',movesLIST')
    # print(attacked_tiles,'value to return')
    return attacked_tiles


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

def handling_players_order(players, player_order_list,*, player_tag = None):
    if player_tag:
        for p in players.values():
            if p.color == player_tag:
                player_order_list.insert(0, player_order_list.pop(player_order_list.index(p)))
                return player_order_list
    else:
        player_order_list.insert(0, player_order_list.pop(-1))
        return player_order_list
