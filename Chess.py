import pygame

from data.chessboard import GameState
from data.constants import GRID_SIZE
from data.game_logic import selecting_piece, get_game_coord_from_mouse, handling_players_order, \
    generating_all_moves_for_piece, looking_for_attacked_tiles
from data.graphic import drawing_board, drawing_pieces
from data.players import Player
from data.settings import FPS

pygame.init()

# INITIZING INSTANCES OF IMPORTED CLASSES
game = GameState()
players_dict = {'player1' : Player(color='w'), 'player2' : Player(color='b')}
player_order_list = list(sorted(players_dict.values(), key=lambda i:('w','b')))
# players = {'player1' : Player(color='w'), 'player2' : Player(color='b')}
# # SETTINGS
# pygame.display.set_caption('Szachy')
# logging.basicConfig(filename='logs.log', level=logging.DEBUG,
#                     format='%(asctime)s,:%(levelname)s:%(module)s:,%(message)s')


def clear_player_data(player):
    player.pins.clear()
    player.attacked_tiles_in_pin.clear()
    player.checks.clear()
    player.attacked_tiles_in_check.clear()



def coords_of_all_player_pieces(player_tag):
    pieces_coord_list = set()
    # board_iter = chain(*game.board)
    # for n, tile in enumerate(board_iter):
    #     if tile and tile.color == player.color:
    #         all_attacked_tiles.update(set(looking_for_absolute_pins(game, tile, coord, player)))
    for col in range(GRID_SIZE):
        for row in range(GRID_SIZE):
            if game.board[row][col] and game.board[row][col].color == player_tag:
                pieces_coord_list.update([(row,col)])
    return pieces_coord_list

def any_move_possible():
    pass

def checking_check(game, base_coord, base_piece, inactive_player):
    for coord in generating_all_moves_for_piece(game, base_piece, base_coord, base_piece.color):
        piece = game.board[coord[1]][coord[0]]
        if piece and piece.color != base_piece.color and piece.tag == 'K':
            inactive_player.in_check = True


def main():
    run = True
    clock = pygame.time.Clock()
    piece_selected = None
    coord_selected = None
    #TODO dodac licznik czasu dla kazdego gracza
    active_player, inactive_player = handling_players_order(players_dict, player_order_list, player_tag=game.nextMoveColor)
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
                # active_player.absolute_pins.clear()
                coord = get_game_coord_from_mouse()
                # TODO dodać narzędzie zarządzające eventami kliknięć itp, na przyszłości do obsługi UI
                if coord is None:  # Resetuje zaznaczenie jeżeli zaznaczy sie puste pole lub kliknie poza board
                    coord_selected = None
                    piece_selected = None
                    break
                if piece_selected is None:
                    piece_selected = selecting_piece(game.board, coord, active_player.color)
                    if piece_selected is not None:
                        possible_moves = generating_all_moves_for_piece(game, piece_selected, coord, active_player)
                        # print('a:',active_player.absolute_pins.items(),'i:',inactive_player.absolute_pins.items())
                        if possible_moves:
                            refresh_flag = True  # zmienna do odswiezania ekranu
                            coord_selected = coord  # zapisuje w pamieci koordynaty prawidlowo wybranej figury
                            # translate_to_chess_notation(possible_moves)
                        else:
                            piece_selected = None  # odznacza figury jak nie ma mozliwosci ruchu lub nieprawidlowy wybor
                elif coord in possible_moves:  # Wchodzi jezeli jest mozliwosc ruchu dla zaznaczonej figury
                    game.new_en_passant_coord = None
                    game.making_move((coord_selected, coord))
                    consequenceFunc = possible_moves[coord]
                    if consequenceFunc is not None:
                        consequenceFunc(game, piece_selected, coord_selected, coord)
                    game.en_passant_coord = game.new_en_passant_coord
                    checking_check(game,coord,piece_selected, inactive_player)
                    drawing_board()
                    drawing_pieces(game.board)

                    active_player.pieces_coords = coords_of_all_player_pieces(active_player.color)
                    '''SZUKANIE SZACHÓW I ZWIAZAN'''
                    clear_player_data(active_player)
                    active_player.all_attacked_tiles = \
                        looking_for_attacked_tiles(game,
                        coords_seq=active_player.pieces_coords,
                        player=inactive_player)
                    print('CHECKS',inactive_player.checks)
                    print('in check', inactive_player.attacked_tiles_in_check)
                    print('PINS',inactive_player.pins)
                    print('in pin', inactive_player.attacked_tiles_in_pin)


                    '''ZMIANA TUR'''
                    active_player, inactive_player = handling_players_order(players_dict, player_order_list)


                    '''SPRAWDZAM CZY JEST MOZLIWY RUCH'''
                    if active_player.checks:
                        active_player.pieces_coords = coords_of_all_player_pieces(active_player.color)
                        print('CHECK')
                        if any(inactive_player.all_attacked_tiles):
                            print('MOVE POSSIBLE')
                        else:
                            print('CHECKMATE')
                    else:
                        # active_player.pieces_coords = coords_of_all_player_pieces(active_player.color)
                        if any(inactive_player.all_attacked_tiles):
                            print('NOT PAT')
                        else:
                            print('PAT')
                        # sprawdz czy inne figury maja ruch w zakresie attacked_fields powiazanych ze zwiazaniem
                        if not any_move_possible():# to przelamania szacha
                            pass
                            # print('CHECKMATE')

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
# 1.attacked_fields nie zawieraja ruchów pionow do przodu trzeba by je dodac jak mam sprawdzac pata
# 2.dodac logike wyszukiwania ruchu w przypadku szacha i szacha podwojnego
# 3.W przypadku zwiazania ograniczyc generowanie ruchow dla zwiazanej figury
# 4.Wykrywanie pata i mata
# - podswietlanie atakowanych pol i ew zwiazan
# podswietlanie wybranej bierki
# podswietlanie ostatnio wykonanego ruchu
# dodac troche grafiki (wspolrzedne, tlo, ui)
# ??? Czy pole króla tez liczyc jao pole atakowane

# later
# 2.interfejs wyboru promowanej figury
# 4.generowac notacje szachowa
# 5.cofanie ruchow
# 8.spradzanie legalnosci roszady
# 9.zegary
