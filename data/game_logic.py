import pygame
from .constants import BOARD_POSITION, TILE_SIZE, BOARD_END_POSITION
# from .pieces import valid_pawn_moves

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

# def listing_valid_moves(piece_selected, piece_coord,target_content, target_coord):# active_player
#     if piece_selected[1] == 'P':
#         valid_moves = valid_pawn_moves(piece_selected, piece_coord, target_content, target_coord)
#         return valid_moves
#     else:
#         pass

def making_move(board, piece_selected, base_coord, target_coord):
    row, col = target_coord
    target_content = board[col][row]
    piece_shift_col = target_coord[0] - base_coord[0]
    piece_shift_row = target_coord[1] - base_coord[1]
    piece_shift = (piece_shift_col, piece_shift_row)
    # valid_moves = listing_valid_moves(piece_selected, base_coord, target_content, target_coord)
    if target_content[0] != piece_selected[0]: #and piece_shift in valid_moves:  pole na które przemieszczam figure musi być puste albo zajęte przez figure przeciwnika
        board[base_coord[1]][base_coord[0]] = "--"
        board[target_coord[1]][target_coord[0]] = piece_selected
        # for i in range(len(board)):
        #     print(board[i])
        # print("\n")
        print("making move", piece_selected[0])
        return None
    else:
        print("not making move")
        return 0

def switching_turns(active_player):
    if active_player == "w":
        return 'b'
    else:
        return "w"
