from .pieces import Pawn, Rook, Knight, Bishop, Queen, King
from .game_logic import sum_directions, multiply_direction

class GameState:
    def __init__ (self):

        self.board = [
            [Rook('b'), Knight('b'), Bishop('b'), Queen('b'), King('b'), Bishop('b'), Knight('b'), Rook('b')],
            [Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b')],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w')],
            [Rook('w'), Knight('w'), Bishop('w'), Queen('w'), King('w'), Bishop('w'), Knight('w'), Rook('w')]]

    def generating_all_moves_for_piece(board, piece, coord, active_player='w'):  # WYPISYWANIE KOLEJNYCH KOLUMN
        moves_list = []
        for j in range(len(piece.movement)):
            for i in range(piece.movement_range):
                increased_piece_movement = multiply_direction(piece.movement[j], i + 1) # i jest mnoznikiem odleglosci
                coords_after_move = sum_directions(coord, increased_piece_movement)
                # if pilnujacy zeby generowane ruchy nie wychodzilo poza zakres planszy
                if min(coords_after_move) >= 0 and max(coords_after_move) < 8:
                    "dodac if zapobiega generowaniu sie wspolrzednych poza polem z bierka przeciwnego koloru?"
                    moves_list.append(increased_piece_movement)
        if not len(moves_list) == 0:
            return moves_list
        else:
            return None

    def __str__(self):
        return '\n'.join(map(','.join, self.board))
