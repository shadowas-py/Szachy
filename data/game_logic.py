import pygame

from .constants import BOARD_POSITION, TILE_SIZE, BOARD_END_POSITION

def sum_directions(direction1, direction2, direction3=(0, 0)):
    return tuple(map(sum, zip(direction1, direction2, direction3)))

def multiply_direction(direction, multiplier):
    multiplied_direction = (direction[0]*multiplier, direction[1]*multiplier)
    return list(multiplied_direction)

def get_game_coord_from_mouse():
    mouse_pos = pygame.mouse.get_pos()
    coord = ((mouse_pos[0] - BOARD_POSITION[1])//TILE_SIZE, (mouse_pos[1] - BOARD_POSITION[0])//TILE_SIZE)
    if BOARD_END_POSITION >= mouse_pos >= BOARD_POSITION:
        return coord
    else:
        return None

# def selecting_piece(board, coord, active_player): # Zwraca None jeżeli nie jest klikniete pole z figura aktywnego gracza
#     row, col = coord
#     piece = board[col][row]
#     if piece[0] == active_player:
#         return piece
#     else:
#         return None

def selecting_piece(board, coord, active_player): # Zwraca None jeżeli nie jest klikniete pole z figura aktywnego gracza
    row, col = coord
    piece = board[col][row]
    if piece != None:  # obiekt nie moze byc None
        if piece.color == active_player:
            return piece
        return None

# def listing_valid_moves(piece_selected, piece_coord,target_content, target_coord):# active_player
#     if piece_selected[1] == 'P':
#         valid_moves = valid_pawn_moves(piece_selected, piece_coord, target_content, target_coord)
#         return valid_moves
#     else:
#         pass

# zeby nie wywalalo jak kliknie sie poza plansze
def making_move(board, piece_selected, base_coord, target_coord, moves_list):
    piece_shift =
    if piece_shift in moves_list:#
        print("test")
        board[base_coord[1]][base_coord[0]] = None
        board[target_coord[1]][target_coord[0]] = piece_selected
        return True
    else:
        return False

def switching_turns(active_player):
    if active_player == "w":
        return 'b'
    else:
        return "w"



