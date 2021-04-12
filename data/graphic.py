import os
import pygame

from .constants import *
from .settings import WIDTH, HEIGHT

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
   
def drawing_board():
    WINDOW.fill(PINK)
    board_white_tiles = pygame.transform.scale(pygame.image.load(
        os.path.join('Images', 'white_tiles.jpg')),
        (B_BACKGROUND_WIDTH, B_BACKGROUND_HEIGHT))
    WINDOW.blit(board_white_tiles, BOARD_BACKGROUND_POSITION)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i+j) % 2 != 0:
                pygame.draw.rect(WINDOW, BROWN, (
                                (TILE_SIZE*i)+BOARD_POSITION[0],
                                (TILE_SIZE*j)+BOARD_POSITION[1],
                                TILE_SIZE, TILE_SIZE))

def drawing_pieces(board):
    for i in range(len(board)):
        print(board[i])
    print("\n")
    for col in range(GRID_SIZE):
        for row in range(GRID_SIZE):
            if board[col][row] != "--":
                tile = str(board[col][row])
                name = GRAPHICS_NAMES[tile]
                piece = pygame.transform.scale(pygame.image.load(
                    os.path.join('Images', name+'.png')),
                    (TILE_SIZE, TILE_SIZE))
                WINDOW.blit(piece, (BOARD_POSITION[0]+(TILE_SIZE*row), BOARD_POSITION[1]+(TILE_SIZE*col)))