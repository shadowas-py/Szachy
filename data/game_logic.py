import pygame

from .constants import BOARD_POSITION, TILE_SIZE, BOARD_END_POSITION, GRID_SIZE
from .functions import sum_directions, multiply_direction

"""ABSOLUTE PINS"""


def get_game_coord_from_mouse():
    mouse_pos = pygame.mouse.get_pos()
    coord = ((mouse_pos[0] - BOARD_POSITION[1]) // TILE_SIZE, (mouse_pos[1] - BOARD_POSITION[0]) // TILE_SIZE)
    if max(BOARD_POSITION) <= min(mouse_pos) and max(mouse_pos) <= min(BOARD_END_POSITION):
        return coord


def selecting_piece(board, coord, player):
    if coord in player.all_possible_moves and any(player.all_possible_moves[coord]):
        return board[coord[1]][coord[0]]


def get_attacked_tiles(vector, start_coord, end_coord):  # end_coord to krol
    attacked_tiles = [start_coord]
    _multiplier = 1
    while end_coord != start_coord:
        start_coord = sum_directions(start_coord, multiply_direction(vector, _multiplier))
        attacked_tiles.append(start_coord)
    return attacked_tiles


def looking_absolute_pins(game, singleMove, occupied_coord, attacking_piece, inactive_player, multiplier):
    for _multiplier in range(multiplier + 1, GRID_SIZE):
        new_coord = sum_directions(attacking_piece.coord, multiply_direction(singleMove, _multiplier))
        if max(new_coord) > 7 or min(new_coord) < 0:
            break
        newPiece = game.board[new_coord[1]][new_coord[0]]
        if newPiece is None:
            continue
        elif newPiece.tag == 'K' and newPiece.color != attacking_piece.color:
            inactive_player.pins[occupied_coord] = attacking_piece.coord
            inactive_player.attacked_tiles_in_pin[attacking_piece.coord] = \
            get_attacked_tiles(vector=singleMove,
                               start_coord=attacking_piece.coord,
                            end_coord=sum_directions(attacking_piece.coord, multiply_direction(singleMove, _multiplier-1)))
            break


def looking_for_attacked_tiles(game, player, inactive_player):  # amd attacked tiles
    attacked_tiles = set()

    for piece in player.pieces:
        if piece.tag == 'P':
            for i in piece.attacked_fields(piece.coord):
                attacked_tiles.update([i])
        else:
            for movePack in piece.movement:
                singleMove, scalable, conditionFunc, consequenceFunc = movePack
                for multiplier in range(1, GRID_SIZE if scalable else 2):
                    new_coord = sum_directions(piece.coord, multiply_direction(singleMove, multiplier))
                    if min(new_coord) < 0 or max(new_coord) >= GRID_SIZE:
                        break
                    elif conditionFunc is None:
                        targetPiece = game.board[new_coord[1]][new_coord[0]]
                        if targetPiece is None:
                            attacked_tiles.update([new_coord])
                        else:
                            if targetPiece.color != piece.color and targetPiece.tag == 'K':
                                print('Zapisuje Szacha')
                                player.checks[piece.coord] = [new_coord]
                                player.attacked_tiles_in_check[new_coord] = get_attacked_tiles(
                                    vector=singleMove,
                                    start_coord=piece.coord,
                                    end_coord=new_coord)
                            elif scalable:
                                looking_absolute_pins(game, multiplier=multiplier,
                                                      singleMove=singleMove,
                                                      inactive_player=inactive_player,
                                                      occupied_coord=new_coord,
                                                      attacking_piece=piece)
                            attacked_tiles.update([new_coord])
                            break
    return attacked_tiles

def validating_moves_in_check(coords, allowed_coords):
    coord_set = set()
    for coord in coords:
        if coord[0] in allowed_coords.values():
            coord_set.update([[coord][0]])
    return


def generating_all_moves_for_piece(game, piece, inactive_player=None, check=False, pin=False):
    moves_list = {}
    base_coord = piece.coord
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
                        # '''DO WYWALENIA Z TĄD??'''
                        # if checks_pins:
                        #     looking_absolute_pins(game, multiplier=multiplier, singleMove=singleMove,
                        #                           player=player, occupied_tile=new_coord, attacker_coord=base_coord)
                    break
            elif conditionFunc(game, piece, base_coord, new_coord):
                moves_list[new_coord] = consequenceFunc
    if check:
        print('in checklist')
        moves_list = validating_moves_in_check(moves_list, inactive_player.attacked_tiles_in_check)
    return moves_list


def handling_players_order(players, player_order_list, *, player_tag=None):
    if player_tag:
        for p in players.values():
            if p.color == player_tag:
                player_order_list.insert(0, player_order_list.pop(player_order_list.index(p)))
                return player_order_list
    else:
        player_order_list.insert(0, player_order_list.pop(-1))
        return player_order_list
