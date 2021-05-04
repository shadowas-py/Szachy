from Szachy.data.constants import N, W, E, S
from .pieces import Pawn, Rook, Knight, Bishop, Queen, King
from .game_logic import sum_directions, multiply_direction


class GameState:
    def __init__(self):
        self.board = [
            [Rook('b'), Knight('b'), Bishop('b'), Queen('b'), King('b'), Bishop('b'), Knight('b'), Rook('b')],
            [Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b')],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w')],
            [Rook('w'), Knight('w'), Bishop('w'), Queen('w'), King('w'), Bishop('w'), Knight('w'), Rook('w')]]

    def generating_all_moves_for_piece(self, board, piece, coord):  # WYPISYWANIE KOLEJNYCH KOLUMN
        # PAWN MOVES
        moves_list = []
        if piece.__class__.__name__ == "Pawn":
            if piece.color == 'w':
                white_pawn_starting_row = 6
                moves_list = []
                new_coord = sum_directions(coord, N)
                if board[new_coord[1]][new_coord[0]] is None:
                    moves_list.append(list(N))
                    new_coord = sum_directions(coord, (sum_directions(N, N)))
                    if coord[1] == white_pawn_starting_row and board[new_coord[1]][new_coord[0]] is None:  # Jezeli pionek znajduje sie w rzedzie startowym
                        moves_list.append(list(sum_directions(N, N)))
                new_coord = sum_directions(coord, (sum_directions(N, W)))
                if board[new_coord[1]][new_coord[0]] is not None and board[new_coord[1]][new_coord[0]].color == 'b':
                    moves_list.append(list(sum_directions(N, W)))
                new_coord = list(sum_directions(coord, (sum_directions(N, E))))
                if board[new_coord[1]][new_coord[0]] is not None and board[new_coord[1]][new_coord[0]].color == 'b':
                    moves_list.append(list(sum_directions(N, E)))
                if len(moves_list) == 0:
                    moves_list = None
                    return moves_list
                else:
                    return moves_list

            elif piece.color == 'b':  # to samo dla czarnego piona
                black_pawn_starting_row = 1
                moves_list = []
                new_coord = sum_directions(coord, S)
                if board[new_coord[1]][new_coord[0]] is None:
                    moves_list.append(list(S))
                    new_coord = sum_directions(coord, (sum_directions(S, S)))
                    if coord[1] == black_pawn_starting_row and board[new_coord[1]][new_coord[0]] is None:  # Jezeli pionek znajduje sie w rzedzie startowym
                        moves_list.append(list(sum_directions(S, S)))
                new_coord = sum_directions(coord, (sum_directions(S, W)))
                if board[new_coord[1]][new_coord[0]] is not None and board[new_coord[1]][new_coord[0]].color == 'w':
                    moves_list.append(list(sum_directions(S, W)))
                new_coord = sum_directions(coord, (sum_directions(S, E)))
                if board[new_coord[1]][new_coord[0]] is not None and board[new_coord[1]][new_coord[0]].color == 'w':
                    moves_list.append(list(sum_directions(S, E)))
                if len(moves_list) == 0:
                    moves_list = None
                    return moves_list
                else:
                    return moves_list
        # REST MOVES
        else:
            for j in range(len(piece.movement)):
                for i in range(piece.movement_range):
                    increased_piece_movement = multiply_direction(piece.movement[j],
                                                                  i + 1)  # i jest mnoznikiem odleglosci
                    coords_after_move = sum_directions(coord, increased_piece_movement)
                    # if pilnujacy zeby generowane ruchy nie wychodzilo poza zakres planszy
                    if min(coords_after_move) >= 0 and max(coords_after_move) < 8:
                        if board[coords_after_move[1]][coords_after_move[0]] != None:
                            # jezeli napotka na przeszkode przerywa iteracje po dlugosci ruchu
                            if board[coords_after_move[1]][coords_after_move[0]].color == piece.color:
                                break
                            else:
                                moves_list.append(increased_piece_movement)
                                break
                        else:
                            moves_list.append(increased_piece_movement)
            if not len(moves_list) == 0:
                return moves_list
            else:
                return None

    def __str__(self):
        return '\n'.join(map(','.join, self.board))
