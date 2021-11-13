import pygame

from data.chess_logger import *
from data.chessboard import GameState
from data.constants import GRID_SIZE
from data.game_logic import get_game_coord_from_mouse, handling_players_order, \
    generating_all_moves_for_piece, looking_for_attacked_tiles, selecting_piece, all_possible_player_moves
from data.graphic import drawing_board, drawing_pieces, draw_markers_in_game_coords
from data.players import Player
from data.settings import FPS

pygame.init()


# SETTING INSTANCES OF IMPORTED CLASSES
game = GameState()
players_dict = {'player1': Player(color='w'), 'player2': Player(color='b')}


def main():
    # INITAL SETTINGS
    run = True
    player_order_list = list(sorted(players_dict.values(), key=lambda i: ('w', 'b')))
    piece_selected = None
    coord_selected = None
    active_player, inactive_player = handling_players_order(players_dict, player_order_list,
                                                            player_tag=game.nextMoveColor)
    # def name_value_log(*args, **kwargs):
    #     vars()['coord']
    #     return (arg for arg in args)


    logger.info('START LOG')
    logger.debug(f'{active_player=} init Player instance')
    logger.debug(f'{inactive_player=} init Player instance')

    active_player.pieces = list(Player.pieces_list(active_player,game))
    logger.debug(f'{active_player.pieces=} len={len(active_player.pieces)}')
    inactive_player.pieces = list(Player.pieces_list(inactive_player,game))
    logger.debug(f'{inactive_player.pieces=} len={len(inactive_player.pieces)}')
    active_player.all_possible_moves = all_possible_player_moves(game, active_player, inactive_player)
    logger.debug(f'{active_player.all_possible_moves}')


    clock = pygame.time.Clock()
    drawing_board()
    drawing_pieces(game.board)
    pygame.display.update()

    while run:
        refresh_flag = False
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:  # LEFT MOUSE BUTTON
                coord = get_game_coord_from_mouse()
                if piece_selected is None:
                    if piece_selected := selecting_piece(game.board, coord, active_player):
                        if possible_moves := active_player.all_possible_moves[piece_selected.coord]:
                            # DRAW ALL ON CHESSBOARD
                            refresh_flag = True
                            coord_selected = coord
                            # translate_to_chess_notation(possible_moves)
                            # logger.info(f'----{possible_moves=}, {active_player.pins=}')
                            # logger.info(f'Wybrano coord{coord} mozliwe ruchy na pola {list(possible_moves.keys())}')

                elif coord in possible_moves:  # Wchodzi jezeli jest mozliwosc ruchu dla zaznaczonej figury
                    logger.info(f'{str(active_player)}'
                                f' {str(piece_selected)}'
                                f' {coord=}'
                                f' {coord_selected}')
                    game.new_en_passant_coord = None
                    """WYKONYWANIE RUCHU"""
                    # print(inactive_player.pieces[])
                    if game.board[coord[1]][coord[0]] in inactive_player.pieces:
                        inactive_player.pieces.remove(game.board[coord[1]][coord[0]])
                    game.making_move((coord_selected, coord))
                    consequenceFunc = possible_moves[coord]
                    piece_selected.coord = coord
                    if consequenceFunc is not None:
                        consequenceFunc(game, piece_selected, coord_selected, coord, player=active_player)
                    game.en_passant_coord = game.new_en_passant_coord
                    game.move_counter+=1

                    logger.info(f'\n{game}')

                    '''CZYSZCZENIE ZWIAZAN I SZACHOWANYCH POL'''
                    active_player.clear_checks_and_pins()

                    '''SZUKANIE ZWIAZAN I SZACHOWANYCH POL'''
                    active_player.all_attacked_tiles = looking_for_attacked_tiles(game,
                                                                                  active_player=active_player,
                                                                                  inactive_player=inactive_player)

                    logger.info(f'{active_player.checks.items()=}'
                                f' {active_player.pins.items()=}'
                                f'{inactive_player.checks.items()=}'
                                f' {inactive_player.pins.items()=}')
                    print('CHECK!!!') if inactive_player.checks else ''
                    '''ZMIANA TUR'''
                    active_player, inactive_player = handling_players_order(players_dict, player_order_list)

                    '''GENEROWANIE RUCHOW DLA KOLEJNEGO GRACZA'''
                    active_player.all_possible_moves = all_possible_player_moves(game,
                                                                                 active_player=active_player,
                                                                                 inactive_player=inactive_player)
                    '''SPRAWDZAM WARUNKI WYGRANEJ'''

                    if active_player.checks and not any(active_player.all_possible_moves.values()):
                        print(f'Wygrał gracz {inactive_player.color.upper()} w {game.move_counter} ruchach')
                    elif not any(active_player.all_possible_moves.values()):
                        print('PAT')
                    piece_selected = None
                    refresh_flag = True

                else:
                    coord_selected = get_game_coord_from_mouse()
                    if piece_selected := selecting_piece(game.board, coord_selected, active_player):
                        possible_moves = active_player.all_possible_moves[piece_selected.coord]
                        refresh_flag = True
        if refresh_flag:
            # if active_player.checks:
            #     drawing_board()
            #     draw_markers_in_game_coords(list(*active_player.checks.values()),color='red')
            #     draw_markers_in_game_coords(list(active_player.checks.keys()),color='blue')
            #     draw_markers_in_game_coords(possible_moves.keys(),color='green')
            #     drawing_pieces(game.board)
            # else:
            drawing_board()
            draw_markers_in_game_coords(inactive_player.all_attacked_tiles, color='red')
            draw_markers_in_game_coords(possible_moves.keys(),color='green')
            if len(active_player.pins) > 1:
                for pin_coords in active_player.pins.values():
                    draw_markers_in_game_coords(game_coords=list(pin_coords), color='blue')
            else:
                draw_markers_in_game_coords(game_coords=list(*active_player.pins.values()), color='blue')
            drawing_pieces(game.board)
            pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
