import pygame
from .constants import BOARD_POSITION, TILE_SIZE, BOARD_END_POSITION

def get_game_coord_from_mouse():
    mouse_pos = pygame.mouse.get_pos()
    coord = ((mouse_pos[0] - BOARD_POSITION[1])//TILE_SIZE, (mouse_pos[1] - BOARD_POSITION[0])//TILE_SIZE)
    if BOARD_END_POSITION >= mouse_pos >= BOARD_POSITION:
        return coord
    else:
        return None

def selecting_piece(board, coord, active_player): # Zwraca None jeżeli nie jest klikniete pole z figura aktywnego gracza
    row, col = coord
    piece = board[col][row]
    if piece[0] == active_player:
        return piece
    else:
        return None

def making_move(board, piece_selected, base_coord, target_coord, ):
    row, col = target_coord
    target_tile = board[col][row]
    if target_tile[0] != piece_selected[0]: # pole na które przemieszczam figure musi być puste albo zajęte przez figure przeciwnika
        print("test")
        board[base_coord[1]][base_coord[0]] = "--"
        board[target_coord[1]][target_coord[0]] = piece_selected
        for i in range(len(board)):
            print(board[i])
        print("\n")
    else:
        return None

def switching_turns(active_player):
    if active_player == "w":
        return 'b'
    else:
        return "w"
