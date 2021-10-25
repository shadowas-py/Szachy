import pygame
import logging

from data.chessboard import GameState
from data.game_logic import selecting_piece, get_game_coord_from_mouse, handling_players_order, \
    generating_all_moves_for_piece, looking_for_absolute_pins
from data.graphic import drawing_board, drawing_pieces
from data.settings import FPS
from data.display_info import translate_to_chess_notation
from data.players import Player
from data.functions import shift_value
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
    print ('clearng')
    for _dict in dicts:
        _dict.clear()

# TODO skrocic to
def generating_all_moves_for_inactive_player(player):
    result = set()
    for col in range(GRID_SIZE):
        for row in range(GRID_SIZE):
            if game.board[col][row] and game.board[col][row].color == player.color:
                coord = (col,row)
                piece = game.board[col][row]
                result.update(set(looking_for_absolute_pins(game, piece, coord, player)))
    return result



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
                coord = get_game_coord_from_mouse()
                # TODO dodać narzędzie zarządzające eventami kliknięć itp, na przyszłości do obsługi UI
                if coord is None:  # Resetuje zaznaczenie jeżeli zaznaczy sie puste pole lub kliknie poza board
                    coord_selected = None
                    piece_selected = None
                    break
                if piece_selected is None:
                    piece_selected = selecting_piece(game.board, coord, active_player.color)
                    if piece_selected is not None:

                        set_of_attacked_fields = generating_all_moves_for_inactive_player(inactive_player)
                        print(list(set_of_attacked_fields))
                        possible_moves = looking_for_absolute_pins(game, piece_selected, coord, active_player)
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
                    # pins_list = generating_pins()
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
# zrobic przeźroczystość pol szachownicy
# podswietlanie wybranej bierki
# podswietlanie ostatnio wykonanego ruchu
# dodac troche grafiki (wspolrzedne, tlo, ui)

# later
# 2.interfejs wyboru promowanej figury
# 4.generowac notacje szachowa
# 5.cofanie ruchow
# 6.sprawdzanie szacha
# 7.sprawdzanie mata i pata
# 8.spradzanie legalnosci roszady
# 9.zegary
