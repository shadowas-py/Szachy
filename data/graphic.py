import os
import pygame

from .settings import WIDTH, HEIGHT
from .pieces import *

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT),pygame.DOUBLEBUF, 32) # Only 32bit surfaces support alpha channel

dark_tile = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'dark_tile.png')),
    (TILE_SIZE, TILE_SIZE))
dark_tile.set_alpha(40)

board_white_tiles = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'white_tiles.jpg')),
    (B_BACKGROUND_WIDTH, B_BACKGROUND_HEIGHT))

def draw_whole_board():
    ... # Funkcja do rysowania odswiezania widoku boarda

def get_colored_square(color, transparency=100):
    marker = pygame.transform.scale(pygame.image.load(
        os.path.join('Images\markers', color + '.png')),(TILE_SIZE, TILE_SIZE))
    marker.set_alpha(transparency)
    return marker

# def get_tile_center(coord):
#     col = (BOARD_POSITION[0] + (TILE_SIZE * coord[0])+TILE_SIZE/2)
#     row = (BOARD_POSITION[1] + (TILE_SIZE * coord[1])+TILE_SIZE/2)
#     return (col,row)

def get_tile_left_top(coord):
    col = (BOARD_POSITION[0] + (TILE_SIZE * coord[0]))
    row = (BOARD_POSITION[1] + (TILE_SIZE * coord[1]))
    return (col,row)

def drawing_coordinates_bar():
    ...

def drawing_board():
    WINDOW.blit(board_white_tiles, BOARD_BACKGROUND_POSITION)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if (row + col) % 2 != 0:
                WINDOW.blit(dark_tile, get_tile_left_top((row,col)))

def drawing_pieces(board):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[col][row] is not None:
                file_name = board[col][row].get_full_name()
                piece = pygame.transform.scale(pygame.image.load(
                    os.path.join('Images', file_name + '.png')),(TILE_SIZE, TILE_SIZE))
                WINDOW.blit(piece, get_tile_left_top((row,col)))

def draw_markers_in_game_coords(game_coords, color='red'):
    '''COLORS : red, blue, green'''
    for coord in game_coords:
        marker=get_colored_square(color)
        WINDOW.blit(marker,(get_tile_left_top(coord)))

