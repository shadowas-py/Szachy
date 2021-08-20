import pygame
import logging

from data.chessboard import GameState
from data.game_logic import selecting_piece, get_game_coord_from_mouse, making_move, switching_turns, \
    disabling_castling_flags
from data.graphic import drawing_board, drawing_pieces
from data.settings import FPS
from data.display_info import translate_to_chess_notation

pygame.init()

# IMPORTS
game = GameState()

# SETTINGS
pygame.display.set_caption('Szachy')
logging.basicConfig(filename='logs.log', level=logging.DEBUG,
                    format='%(asctime)s,:%(levelname)s:%(module)s:,%(message)s')


def main():
    run = True
    clock = pygame.time.Clock()
    possible_target_tiles = None
    piece_selected = None
    coord_selected = None
    active_player = 'w'
    drawing_board()
    drawing_pieces(game.board)
    pygame.display.update()
    while run:
        refresh_flag = False
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:  # jezeli wcisniety LEFT MOUSE BUTTON
                coord = get_game_coord_from_mouse()
                # TODO dodac narzedzie zarzadzajace eventami klikniec itp, na przyszlosc do obslugi UI
                if coord is None:  # Resetuje zaznaczenie jezeli zaznaczy sie puste pole lub kliknie poza board
                    coord_selected = None
                    piece_selected = None
                    break
                if piece_selected is None:  # Wchodzi jeżeli nic nie jest zaznaczone
                    piece_selected = selecting_piece(game.board, coord, active_player)
                    if piece_selected is not None:  # Sprawdzam czy sa mozliwe ruchy dla danego zaznaczenia
                        possible_target_tiles = game.generating_all_moves_for_piece(game.board, piece_selected, coord)
                        if possible_target_tiles is not None:
                            refresh_flag = True  # zmienna do odswiezania ekranu
                            coord_selected = coord  # zapisuje w pamieci koordynaty prawidlowo wybranej figury
                            translate_to_chess_notation(possible_target_tiles)
                        else:
                            piece_selected = None  # odznacza figury jak nie ma mozliwosci ruchu lub nieprawidlowy wybor
                elif coord in possible_target_tiles:  # Wchodzi jezeli jest mozliwosc ruchu dla zaznaczonej figury
                    single_move_sequence = [(coord_selected, coord)]
                    if coord != possible_target_tiles[-1] and \
                            type(possible_target_tiles[possible_target_tiles.index(coord) + 1][0]) is tuple:
                        single_move_sequence.append(possible_target_tiles[possible_target_tiles.index(coord)+1])
                    making_move(game.board, single_move_sequence)
                    if piece_selected.tag == 'K' or piece_selected.tag == 'R':
                        disabling_castling_flags(game=game, piece=piece_selected, base_coord=coord_selected)
                    drawing_board()
                    drawing_pieces(game.board)
                    active_player = switching_turns(active_player)
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
# 2.Promocja piona (interfejs wyboru figury)
# 3.Bicie w przelocie
# 4.generowac notacje szachowa
# 5.cofanie ruchow
# 6.sprawdzanie szacha
# 7.sprawdzanie mata i pata
# 8.spradzanie legalnosci roszady
# 9.zegary
