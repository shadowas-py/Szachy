import pygame

from data.chessboard import GameState
from data.constants import GRID_SIZE
from data.game_logic import get_game_coord_from_mouse, handling_players_order, \
    generating_all_moves_for_piece, looking_for_attacked_tiles, selecting_piece
from data.graphic import drawing_board, drawing_pieces
from data.players import Player
from data.settings import FPS

pygame.init()

# INITIZING INSTANCES OF IMPORTED CLASSES
game = GameState()
players_dict = {'player1': Player(color='w'), 'player2': Player(color='b')}
player_order_list = list(sorted(players_dict.values(), key=lambda i: ('w', 'b')))


# players = {'player1' : Player(color='w'), 'player2' : Player(color='b')}
# # SETTINGS
# pygame.display.set_caption('Szachy')
# logging.basicConfig(filename='logs.log', level=logging.DEBUG,
#                     format='%(asctime)s,:%(levelname)s:%(module)s:,%(message)s')

def clear_player_data(player):
    player.pins.clear()
    player.checks.clear()
    player.attacked_tiles_in_check.clear()
    player.all_possible_moves.clear()


# def coords_of_all_player_pieces(player_tag):
#     pieces_coord_list = set()
#     for col in range(GRID_SIZE):
#         for row in range(GRID_SIZE):
#             if game.board[row][col] and game.board[row][col].color == player_tag:
#                 pieces_coord_list.update([(row,col)])
#     return pieces_coord_list

def all_possible_moves(game, player):
    for piece in player.pieces_list:
        print(piece, 'test')


'''DO PRZEROBIENIA'''


# def checking_check(game, piece_selected, inactive_player):
#     for coord in generating_all_moves_for_piece(game, piece_selected):
#         piece = game.board[coord[1]][coord[0]]
#         if piece and piece.color != piece_selected.color and piece.tag == 'K':
#             inactive_player.in_check = True


def pieces_list(game, player):
    for col in range(GRID_SIZE):
        for row in range(GRID_SIZE):
            if game.board[row][col] and game.board[row][col].color == player.color:
                yield game.board[row][col]


def all_possible_player_moves(game, active_player, inactive_player, pin=False):
    moves_list = {}
    for piece in active_player.pieces:
        moves_list[piece.coord] = generating_all_moves_for_piece(game, piece,
                                                                 inactive_player=active_player,
                                                                 check=any(inactive_player.checks))
    return moves_list


def main():
    run = True
    clock = pygame.time.Clock()
    piece_selected = None
    coord_selected = None
    active_player, inactive_player = handling_players_order(players_dict, player_order_list,
                                                            player_tag=game.nextMoveColor)
    active_player.pieces = list(pieces_list(game, active_player))
    inactive_player.pieces = list(pieces_list(game, inactive_player))
    active_player.all_possible_moves = all_possible_player_moves(game, active_player, inactive_player)
    drawing_board()
    drawing_pieces(game.board)
    '''Wywalic jak zbedne'''
    # active_player.all_attacked_tiles = \
    #     looking_for_attacked_tiles(game, coords_seq=coords_of_all_player_pieces(inactive_player.color), player=inactive_player)
    pygame.display.update()
    while run:
        refresh_flag = False
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:  # LEFT MOUSE BUTTON
                coord = get_game_coord_from_mouse()
                if piece_selected is None:
                    if piece_selected := selecting_piece(game.board, coord, active_player):
                        if possible_moves := active_player.all_possible_moves[piece_selected.coord]:
                            refresh_flag = True
                            coord_selected = coord
                            # translate_to_chess_notation(possible_moves)
                elif coord in possible_moves:  # Wchodzi jezeli jest mozliwosc ruchu dla zaznaczonej figury
                    game.new_en_passant_coord = None
                    """WYKONYWANIE RUCHU"""
                    game.making_move((coord_selected, coord))
                    consequenceFunc = possible_moves[coord]
                    piece_selected.coord = coord
                    if consequenceFunc is not None:
                        consequenceFunc(game, piece_selected, coord_selected, coord)
                    game.en_passant_coord = game.new_en_passant_coord
                    # checking_check(game, piece_selected, inactive_player)
                    drawing_board()
                    drawing_pieces(game.board)
                    '''CLEAR ACTIVE PLAYER DATA'''
                    clear_player_data(active_player)

                    '''SZUKANIE ZWIAZAN I SZACHOWANYCH POL'''
                    active_player.all_attacked_tiles = looking_for_attacked_tiles(game,
                                                                                  player=active_player,
                                                                                  inactive_player=inactive_player)
                    """GENEROWANIE RUCHOW DLA NASTEPNEGO GRACZA"""
                    inactive_player.all_possible_moves = all_possible_player_moves(game,
                                                                                   active_player=inactive_player,
                                                                                   inactive_player=active_player)

                    # print(inactive_player.all_possible_moves)

                    # print(list(active_player.pieces))
                    # print(inactive_player.all_attacked_tiles, 'all_attacked_tiles',active_player.all_attacked_tiles)
                    print('CHECKS', inactive_player.checks, active_player.checks)
                    print('inCHeck', inactive_player.attacked_tiles_in_check, active_player.attacked_tiles_in_check)
                    print('PINS', inactive_player.pins, active_player.pins)
                    # print('in pin', inactive_player.attacked_tiles_in_pin)

                    '''ZMIANA TUR'''
                    active_player, inactive_player = handling_players_order(players_dict, player_order_list)

                    # active_player.pieces = pieces_list(game, active_player)
                    # inactive_player.pieces = pieces_list(game, inactive_player)

                    '''SPRAWDZAM CZY JEST MOZLIWY RUCH'''

                    # sprawdz czy inne figury maja ruch w zakresie attacked_fields powiazanych ze zwiazaniem
                    # if not any_move_possible():# to przelamania szacha
                    #     pass
                    #     # print('CHECKMATE')

                    piece_selected = None
                    refresh_flag = True
                else:
                    coord_selected = get_game_coord_from_mouse()
                    if piece_selected := selecting_piece(game.board, coord_selected, active_player):
                        possible_moves = active_player.all_possible_moves[piece_selected.coord]

        if refresh_flag:
            pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()

# TODO
# 2.dodac logike wyszukiwania ruchu w przypadku szacha i szacha podwojnego
# 3.W przypadku zwiazania ograniczyc generowanie ruchow dla zwiazanej figury
# 4.Wykrywanie pata i mata
# 5.Dodac czas dla graczy
# - podswietlanie atakowanych pol i ew zwiazan
# podswietlanie wybranej bierki
# podswietlanie ostatnio wykonanego ruchu
# dodac troche grafiki (wspolrzedne, tlo, ui)
# ??? Czy pole króla tez liczyc jao pole atakowane
# TODO dodać narzędzie zarządzające eventami kliknięć itp, na przyszłości do obsługi UI

# later
# 2.interfejs wyboru promowanej figury
# 4.generowac notacje szachowa
# 5.cofanie ruchow
# 8.spradzanie legalnosci roszady
# 9.zegary
