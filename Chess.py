import pygame
import logging
from itertools import chain


from data.chessboard import GameState
from data.game_logic import selecting_piece, get_game_coord_from_mouse, handling_players_order, \
    generating_all_moves_for_piece, looking_for_attacked_fields
from data.graphic import drawing_board, drawing_pieces
from data.settings import FPS
from data.display_info import translate_to_chess_notation
from data.players import Player
from data.constants import GRID_SIZE

pygame.init()

# INITIZING INSTANCES OF IMPORTED CLASSES
game = GameState()
players_dict = {'player1' : Player(color='w'), 'player2' : Player(color='b')}
player_order_list = list(sorted(players_dict.values(), key=lambda i:('w','b')))
# players = {'player1' : Player(color='w'), 'player2' : Player(color='b')}
# # SETTINGS
# pygame.display.set_caption('Szachy')
# logging.basicConfig(filename='logs.log', level=logging.DEBUG,
#                     format='%(asctime)s,:%(levelname)s:%(module)s:,%(message)s')


def clear_data(*dicts):
    for _dict in dicts:
        _dict.clear()

def all_same_color_pieces(player_tag):
    all_attacked_tiles = set()
    # board_iter = chain(*game.board)
    # for n, tile in enumerate(board_iter):
    #     if tile and tile.color == player.color:
    #         all_attacked_tiles.update(set(looking_for_absolute_pins(game, tile, coord, player)))
    for col in range(GRID_SIZE):
        for row in range(GRID_SIZE):
            real_coord = col, row
            if game.board[row][col] and game.board[row][col].color == player_tag:
                piece = game.board[row][col]
                all_attacked_tiles.update(set(looking_for_attacked_fields(game, piece, real_coord)))
                # input(f'{real_coord}real coord')
    return all_attacked_tiles


def any_move_possible():
    pass


def main():
    run = True
    clock = pygame.time.Clock()
    piece_selected = None
    coord_selected = None
    #TODO dodac liczbnik czasu dla kazdego gracza
    # active_player = players_dict['player1'] if game.nextMoveColor is 'w' else players_dict['player2']
    active_player, inactive_player = handling_players_order(players_dict, player_order_list, player_tag=game.nextMoveColor)
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
                active_player.absolute_pins.clear()
                """DOKONCZYC"""
                all_attacked_tiles = all_same_color_pieces(inactive_player.color)
                coord = get_game_coord_from_mouse()
                # TODO dodać narzędzie zarządzające eventami kliknięć itp, na przyszłości do obsługi UI
                if coord is None:  # Resetuje zaznaczenie jeżeli zaznaczy sie puste pole lub kliknie poza board
                    coord_selected = None
                    piece_selected = None
                    break
                if piece_selected is None:
                    piece_selected = selecting_piece(game.board, coord, active_player.color)
                    if piece_selected is not None:
                        possible_moves = generating_all_moves_for_piece(game, piece_selected, coord, active_player)
                        print('a:',active_player.absolute_pins.items(),'i:',inactive_player.absolute_pins.items())
                        if possible_moves:
                            refresh_flag = True  # zmienna do odswiezania ekranu
                            coord_selected = coord  # zapisuje w pamieci koordynaty prawidlowo wybranej figury
                            # translate_to_chess_notation(possible_moves)
                        else:
                            piece_selected = None  # odznacza figury jak nie ma mozliwosci ruchu lub nieprawidlowy wybor
                elif coord in possible_moves:  # Wchodzi jezeli jest mozliwosc ruchu dla zaznaczonej figury
                    game.new_en_passant_coord = None
                    game.making_move((coord_selected, coord))
                    consequenceFunc = possible_moves[coord]
                    if consequenceFunc is not None:
                        consequenceFunc(game, piece_selected, coord_selected, coord)
                    game.en_passant_coord = game.new_en_passant_coord
                    drawing_board()
                    drawing_pieces(game.board)
                    active_player, inactive_player = handling_players_order(players_dict, player_order_list)
                    if any_move_possible() is False:print('PAT')
                    piece_selected = None
                    refresh_flag = True
                else:
                    piece_selected = None
        if refresh_flag:
            pygame.display.update()
    pygame.quit()





if __name__ == "__main__":
    main()

#TODO
# 4.dodac do do kklasy player atrybut-slownik ze wspolrzednymi bierki zwiazujacej : lista pol miedzy nia a wrogim krolem
# - podswietlanie atakowanych pol i ew zwiazan
# podswietlanie wybranej bierki
# podswietlanie ostatnio wykonanego ruchu
# dodac troche grafiki (wspolrzedne, tlo, ui)
# ??? Czy pole króla tez liczyc jao pole atakowane

# later
# 2.interfejs wyboru promowanej figury
# 4.generowac notacje szachowa
# 5.cofanie ruchow
# 6.sprawdzanie szacha
# 7.sprawdzanie mata i pata
# 8.spradzanie legalnosci roszady
# 9.zegary
