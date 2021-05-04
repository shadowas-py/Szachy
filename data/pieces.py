from .game_logic import sum_directions
from .constants import N, S, W, E, GRID_SIZE


# """WYCZYSCIC LISTE DOSTEPNYCH RUCHOW JEZELI NIE MA ZADNYCH RUCHOW LUB KLIKNIETE
#  BEDZIE POLE NIEDOSTEPNE NA LISCIE DOZWOLONYXH RUCHOW"""
# def listing_moves_for_the_piece(piece_movement, movement_range, piece_coord):
#     moves_list = []
#     for j in range(len(piece_movement)):
#         for i in range(movement_range):
#             increased_piece_movement = multiply_direction(piece_movement[j], i+1)  # kierunek ruchu z mnoznikiem 'i'
#             coords_after_move = sum_directions(piece_coord, increased_piece_movement)
#             # if pilnujacy zeby generowane ruchy nie wychodzilo poza zakres planszy
#             if min(coords_after_move) >= 0 and max(coords_after_move) < 8:
#                 "dodac if zapobiega generowaniu sie wspolrzednych poza polem z bierka przeciwnego koloru?"
#                 moves_list.append(increased_piece_movement)
#     return moves_list

# class Pieces:
#     def __init__(self, board, piece_coord, piece_selected):
#         self.piece_color = piece_selected[0]
#         self.piece_coord = piece_coord
#         self.board = board

    # def swap_piece_symbol_to_object(self, piece_selected):# sam symbol figury bez koloru
    #
    #     if piece_selected == "P":
    #         piece_object = Pawn(self.board, self.piece_color, self.piece_coord)
    #     elif piece_selected == "R":
    #         piece_object = Rook(self.board, self.piece_color,self.piece_coord)
    #     elif piece_selected == "N":
    #         piece_object = Knight(self.board, self.piece_color,self.piece_coord)
    #     elif piece_selected == "B":
    #         piece_object = Bishop(self.board, self.piece_color,self.piece_coord)
    #     elif piece_selected == "Q":
    #         piece_object = Queen(self.board, self.piece_color,self.piece_coord)
    #     elif piece_selected == "K":
    #         piece_object = King(self.board, self.piece_color,self.piece_coord)
    #
    #     # PIECE_OBJECTS = {'P': Pawn(self.board, self.piece_color, self.piece_coord),
    #     #                  'R': Rook(self.board, self.piece_color,self.piece_coord),
    #     #                  'N': Knight(self.board, self.piece_color,self.piece_coord),
    #     #                  'B': Bishop(self.board, self.piece_color,self.piece_coord),
    #     #                  'Q': Queen(self.board, self.piece_color,self.piece_coord),
    #     #                  'K': King(self.board, self.piece_color,self.piece_coord),
    #     #                  }
    #     # return PIECE_OBJECTS[piece_selected]
    #     # sam symbol figury bez koloru
    #     return piece_object

class Pawn:
    """zrobic zczytywanie wspolrzednych obiektu"""
    # nie moge generowac ruchow Piona tutaj bo potrzebuje jego wspolrzedne i kompleatny stan boarda
    def __init__(self, color): # domyslna ilosc pól o jakie dana figura moze sie poruszac
        self.color = color
        #MOVEMENT
        self.movement_range = 1
        if self.color == 'b':
            self.file_name = 'black_pawn'
        else:
            self.file_name = 'white_pawn'
        #TO DO
        #bicie w przelocie

class King:
    def __init__(self, color): # parametry do poprawienia
        self.color = color
        self.movement_range = 1
        self.movement = N, S, E, W, \
                          sum_directions(N, E), sum_directions(N, W), sum_directions(S, W), sum_directions(S, W)

        if self.color == 'b':
            self.file_name = 'black_king'
        else:
            self.file_name = 'white_king'
        # self.all_moves = listing_moves_for_the_piece(self.movement, self.movement_range, piece_coord)
        # TO DO
        # dodac znaczniki i ruch roszady dla bialego i czarnego

class Rook:
    def __init__(self, color):
        self.color = color
        self.movement_range = GRID_SIZE-1
        self.movement = N, S, E, W

        # GRAPHIC
        if self.color == 'b':
            self.file_name = 'black_rook'
        else:
            self.file_name = 'white_rook'
        # self.all_moves = listing_moves_for_the_piece(self.movement, self.movement_range, piece_coord)

class Knight:
    def __init__(self, color):
        self.color = color
        self.movement_range = 1
        self.movement = sum_directions(N, N, E), sum_directions(N, N, W), \
                          sum_directions(E, E, N), sum_directions(E, E, S), \
                          sum_directions(W, W, N), sum_directions(W, W, S), \
                          sum_directions(S, S, E), sum_directions(S, S, W)

        if self.color == 'b':
            self.file_name = 'black_knight'
        else:
            self.file_name = 'white_knight'

        # self.all_moves = listing_moves_for_the_piece(self.movement, self.movement_range, piece_coord)

class Bishop:
    def __init__(self, color):
        self.color = color
        self.movement_range = GRID_SIZE-1
        self.movement = sum_directions(N, E), sum_directions(N, W), \
                          sum_directions(S, E), sum_directions(S, W), \

        if self.color == 'b':
            self.file_name = 'black_bishop'
        else:
            self.file_name = 'white_bishop'
        # self.all_moves = listing_moves_for_the_piece(self.movement, self.movement_range, piece_coord)

class Queen:
    def __init__(self, color):
        self.color = color
        self.movement_range = GRID_SIZE-1
        self.movement = N, S, E, W, sum_directions(N, E), sum_directions(N, W), \
                          sum_directions(S, E), sum_directions(S, W), \

        if self.color == 'b':
            self.file_name = 'black_queen'
        else:
            self.file_name = 'white_queen'
        # self.all_moves = listing_moves_for_the_piece(self.movement, self.movement_range, piece_coord)
