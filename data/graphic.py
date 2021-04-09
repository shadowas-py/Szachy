import pygame, os
from .constants import *
from .settings import WIDTH, HEIGHT

#IMPORTS
# game = Game()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
   
def drawing_board():
    # DRAWING BOARD
    from .chessboard import Game
    WINDOW.fill(PINK)
    BOARD_WHITE_BG = pygame.transform.scale(pygame.image.load(
        os.path.join('F:\projekty\Szachy VS\Images','white_tiles.jpg')),
        (B_BACKGROUND_WIDTH, B_BACKGROUND_HEIGHT))
    WINDOW.blit(BOARD_WHITE_BG, (BOARD_BACKGROUND_POSITION))
    for i in range (GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i+j)%2 != 0:
                pygame.draw.rect(WINDOW, BROWN,(
                                (TILE_SIZE*i)+BOARD_POSITION[0],
                                (TILE_SIZE*j)+BOARD_POSITION[1],
                                TILE_SIZE, TILE_SIZE))
    pygame.display.update()

def drawing_pieces(board):
    for i in range (len(board)):
        print(board[i])
    print("\n")
    for col in range (GRID_SIZE):
        for row in range (GRID_SIZE):
            if board[col][row] != "--":
                tile = str(board[col][row])
                name = GRAPHICS_NAMES[tile]
                piece = pygame.transform.scale(pygame.image.load(
                    os.path.join('Images', name+'.png')),
                    (TILE_SIZE, TILE_SIZE))
                WINDOW.blit(piece,(BOARD_POSITION[0]+(TILE_SIZE*row), BOARD_POSITION[1]+(TILE_SIZE*col)))
    pygame.display.update()
