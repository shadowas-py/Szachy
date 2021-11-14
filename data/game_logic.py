import pygame

from logs.loggers import debug_pins

from .constants import BOARD_POSITION, TILE_SIZE, BOARD_END_POSITION, GRID_SIZE
from .functions import sum_directions, multiply_direction


def get_game_coord_from_mouse():
    mouse_pos = pygame.mouse.get_pos()
    coord = ((mouse_pos[0] - BOARD_POSITION[1]) // TILE_SIZE, (mouse_pos[1] - BOARD_POSITION[0]) // TILE_SIZE)
    if max(BOARD_POSITION) <= min(mouse_pos) and max(mouse_pos) <= min(BOARD_END_POSITION):
        return coord

def selecting_piece(board, coord, player):
    if coord in player.all_possible_moves and any(player.all_possible_moves[coord]):
        return board[coord[1]][coord[0]]

def get_attacked_tiles(vector,start_coord,end_coord): #  end_coord to krol
    attacked_tiles = [start_coord]
    _multiplier = 1
    while end_coord != start_coord:
        start_coord = sum_directions(start_coord, multiply_direction(vector, _multiplier))
        attacked_tiles.append(start_coord)
    return attacked_tiles

def looking_absolute_pins(game, singleMove, occupied_coord, attacking_piece, inactive_player, multiplier):
    debug_pins.info(f'{singleMove=},'
                    f' FIRST OCCUPIED: {occupied_coord} {game.board[occupied_coord[1]][occupied_coord[0]].get_full_name()}'
                    f' ATTACKER: {attacking_piece.get_full_name()},'
                    f' {inactive_player.color=}, {multiplier=}')

    for _multiplier in range(multiplier + 1, GRID_SIZE):
        new_coord = sum_directions(attacking_piece.coord, multiply_direction(singleMove, _multiplier))
        if max(new_coord) > 7 or min(new_coord) < 0:
            break
        newPiece = game.board[new_coord[1]][new_coord[0]]
        debug_pins.info(f'  {new_coord=}, {newPiece.get_full_name() if newPiece else None}')

        if newPiece is None:
            debug_pins.info(f'  CONTINUE')
            continue

        elif newPiece.tag == 'K' and newPiece.color != attacking_piece.color:
            inactive_player.pins[occupied_coord] = get_attacked_tiles(vector=singleMove,
                                                                      start_coord=attacking_piece.coord,
                                                                      end_coord=sum_directions(
                                                                          attacking_piece.coord,
                                                                          multiply_direction(singleMove, _multiplier-1)))
            debug_pins.info(f'  SETTING PIN')
        break

def looking_for_attacked_tiles(game, active_player, inactive_player):
    attacked_tiles = set()
    for piece in active_player.pieces:
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
                        attacked_tiles.update([new_coord])
                        if targetPiece:
                            if targetPiece.color != piece.color and targetPiece.tag == 'K':
                                tiles = get_attacked_tiles(
                                    vector=singleMove,
                                    start_coord=piece.coord,
                                    end_coord=new_coord)
                                #FIXME  # NIE SKALOWANIE SKOCZKA PIONA ITP PRZY SZUKANIU SZACHOW - chyba do tego ten kod
                                # cd = sum_directions(tiles[0], multiply_direction(singleMove, multiplier+2))
                                # if max(cd)<8 and min(cd)>=0 and game.board[cd[1]][cd[0]] is None :
                                #     print('IN')
                                #     attacked_tiles.update([sum_directions(tiles[0], multiply_direction(singleMove, multiplier+1))])
                                inactive_player.checks[piece.coord] = tiles[:-1]

                            elif scalable:
                                looking_absolute_pins(game, multiplier=multiplier,
                                                      singleMove=singleMove,
                                                      inactive_player=inactive_player,
                                                      occupied_coord=new_coord,
                                                      attacking_piece=piece)
                            if targetPiece.color != piece.color and targetPiece.tag != 'K' \
                                or targetPiece.color == piece.color:
                                break
    return attacked_tiles

def validating_moves(moves_list, allowed_coords):
    for coord in list(moves_list):
        if coord not in allowed_coords:
            moves_list.pop(coord)
    return moves_list

def generating_all_moves_for_piece(game, piece, inactive_player=None, check=False, active_player=None):
    moves_list = {}
    if check and inactive_player.pins and piece.coord in inactive_player.pins.keys():
        return moves_list
    for movePack in piece.movement:
        singleMove, scalable, conditionFunc, consequenceFunc = movePack
        for multiplier in range(1, GRID_SIZE if scalable else 2):
            new_coord = sum_directions(piece.coord, multiply_direction(singleMove, multiplier))
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
            elif conditionFunc(game, piece, new_coord=new_coord, attacked_tiles=active_player.all_attacked_tiles):
                moves_list[new_coord] = consequenceFunc
    if check:
        if piece.tag == 'K':
            moves_list = {k : moves_list[k] for k in set(moves_list) - set(active_player.all_attacked_tiles) }
        else:
            moves_list = validating_moves(moves_list, *inactive_player.checks.values())

    elif piece.tag == 'K':
        moves_list = {k : moves_list[k] for k in set(moves_list) - set(active_player.all_attacked_tiles) }
    if inactive_player.pins and piece.coord in inactive_player.pins.keys():
        moves_list = validating_moves(moves_list, inactive_player.pins[piece.coord])
    return moves_list

def all_possible_player_moves(game, active_player, inactive_player, pin=False):
    moves_list = {}
    for piece in active_player.pieces:
        moves_list[piece.coord] = generating_all_moves_for_piece(game, piece,
                                                                 inactive_player=active_player,
                                                                 active_player=inactive_player,
                                                                 check=any(active_player.checks))
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
