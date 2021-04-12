import pygame
from data.constants import *
from data.chessboard import Game
from data.settings import *
from data.game_logic import *
from data.graphic import *

pygame.init()

# IMPORTS
game = Game()

# SETTINGS
pygame.display.set_caption('Szachy')


def main():
    run = True
    clock = pygame.time.Clock()
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
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0]:  # jezeli wcisniety LEFT MOUSE BUTTON
                coord = get_game_coord_from_mouse()
                if piece_selected is None:  # Wchodzi jeżeli nic nie jest zaznaczone
                    piece_selected = selecting_piece(game.board, coord, active_player)
                    if piece_selected is not None:
                        refresh_flag = True
                        coord_selected = coord
                elif piece_selected != None:  # Wchodzi jeżeli zaznaczona jest jakas figura
                    if making_move(game.board, piece_selected, coord_selected, target_coord=coord) is None:
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

# przezroczystosc pol
# 1.Zdefiniowac figury
# 2.Promocja piona
# 3.Bicie w przelocie