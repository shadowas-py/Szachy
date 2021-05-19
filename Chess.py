import pygame
import logging

from Szachy.data.chessboard import GameState
from Szachy.data.game_logic import selecting_piece, get_game_coord_from_mouse, making_move, switching_turns
from Szachy.data.graphic import drawing_board, drawing_pieces
# from Szachy.data.pieces import Pieces
from Szachy.data.settings import FPS

pygame.init()

# IMPORTS
game = GameState()
print(game.board)

# SETTINGS
pygame.display.set_caption('Szachy')
logging.basicConfig(filename='logs.log', level=logging.DEBUG,
                    format = '%(asctime)s,:%(levelname)s:%(module)s:,%(message)s')

def main():
    run = True
    clock = pygame.time.Clock()
    possible_moves = None
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
                if piece_selected is None:  # Wchodzi jeżeli nic nie jest zaznaczone
                    piece_selected = selecting_piece(game.board, coord, active_player)
                    if piece_selected is not None: # Sprawdzam czy nie zaznaczam None
                        '''moznaby przypisac coord do obiektu piece'''
                        possible_moves = game.generating_all_moves_for_piece(game.board, piece_selected, coord)
                        if possible_moves is not None:
                            refresh_flag = True# zmienna do odswiezania ekranu
                            coord_selected = coord # zapisuje w pamieci koordynaty prawidlowo wybranej figury
                        else:
                            piece_selected = None  # odznacza figury jak nie ma mozliwosci ruchu
                    print(possible_moves)
                    '''if piece_shift in moves_list(possible_moves) TO WSTAWIC GDZIES TUTAJ'''
                elif possible_moves is not None:  # Wchodzi jezeli jest mozliwosc ruchu dla zaznaczonej figury
                    if making_move(game.board, piece_selected, coord_selected, coord, possible_moves) is True:
                        # ruch sie bedzie wykonywal jezeli bedzie na liscie moves allowed
                        drawing_board()
                        drawing_pieces(game.board)
                        active_player = switching_turns(active_player)
                    piece_selected = None
                    refresh_flag = True
        if refresh_flag:
            pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()

#TO DO
# zrobic przeźroczystość pol szachownicy
# podswietlanie wybranej bierki
# podswietlanie ostatnio wykonanego ruchu
# dodac troche grafiki (wspolrzedne, tlo, ui)
# 1.Roszady(bez sprawdzania legalnosci)

#later
# uporzadkowac kod generujacy ruchy - Pawn
# 2.Promocja piona (interfejs wyboru figury)
# 3.Bicie w przelocie
# 4.generowac notacje szachowa
# 5.cofanie ruchow
# 6.sprawdzanie szacha
# 7.sprawdzanie mata i pata
# 8.spradzanie legalnosci roszady
# 8.zegary

# Knows bugs
#. Klikniecie poza szachownice crashuje
