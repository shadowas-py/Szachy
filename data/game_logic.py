import pygame

from .constants import BOARD_POSITION, TILE_SIZE, BOARD_END_POSITION, GRID_SIZE
from .functions import sum_directions, multiply_direction

"""ABSOLUTE PINS"""

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

def looking_for_absolute_pins(game, multiplier, singleMove, occupied_tile, base_coord, player):
    for _multiplier in range(multiplier+1, GRID_SIZE):
        new_coord = sum_directions(base_coord, multiply_direction(singleMove, _multiplier))
        if max(new_coord)>7 or min(new_coord)<0:
            break
        targetPiece = game.board[new_coord[1]][new_coord[0]]
        if targetPiece is None:
            continue
        elif targetPiece.tag == 'K' and targetPiece.color != player.color :
            player.absolute_pins[occupied_tile]=base_coord
            break
        else:
            break


def looking_for_attacked_fields(game, piece, base_coord): # amd attacked tiles
    attacked_tiles = set()
    # print(piece, 'picked_piece', base_coord)
    if piece.tag == 'P':
        for i in piece.attacked_fields(base_coord):
            # print('SET', base_coord, piece, i)
            attacked_tiles.update([i])
    else:
        for movePack in piece.movement:
            singleMove, scalable, conditionFunc, consequenceFunc = movePack
            for multiplier in range(1, GRID_SIZE if scalable else 2):
                new_coord = sum_directions(base_coord, multiply_direction(singleMove, multiplier))
                if min(new_coord) < 0 or max(new_coord) >= GRID_SIZE:
                    break
                elif conditionFunc is None:
                    targetPiece = game.board[new_coord[1]][new_coord[0]]
                    if targetPiece is None:
                        attacked_tiles.update([new_coord])
                    else:
                        if targetPiece.color != piece.color:
                            # print('SET coord:','targer_coord:',new_coord, 'target:',targetPiece,'active:', piece)
                            attacked_tiles.update([new_coord])
                            break
                        else:
                            # print('SET same_color', new_coord,targetPiece, 'NEW COORD',piece )
                            attacked_tiles.update([new_coord])
                            break
        # print(attacked_tiles,'value to return')
    return attacked_tiles


def generating_all_moves_for_piece(game, piece, base_coord, player):
    moves_list = {}
    for movePack in piece.movement:
        singleMove, scalable, conditionFunc, consequenceFunc = movePack
        for multiplier in range(1, GRID_SIZE if scalable else 2):
            new_coord = sum_directions(base_coord, multiply_direction(singleMove, multiplier))
            if min(new_coord) < 0 or max(new_coord) >= GRID_SIZE:
                break
            elif conditionFunc is None:
                targetPiece = game.board[new_coord[1]][new_coord[0]]
                if targetPiece is None:
                    moves_list[new_coord] = consequenceFunc
                else:
                    if targetPiece.color != piece.color:
                        moves_list[new_coord] = consequenceFunc
                        looking_for_absolute_pins(game, multiplier, singleMove,
                                                  player=player, occupied_tile=new_coord, base_coord=base_coord )
                    break
            elif conditionFunc(game, piece, base_coord, new_coord):
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
