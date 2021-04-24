from .pieces import Pawn


def convert_piece_string_to_object(board, piece_coord, picked_piece):

    Pieces_list = {'wP': Pawn(game.board,piece_coord, piece_selected),
                      'wR': Pawn(game.board, piece_coord, piece_selected),
                      'wN': Pawn(game.board, piece_coord, piece_selected),
                      'wB': Pawn(game.board, piece_coord, piece_selected),
                      'wQ': Pawn(game.board, piece_coord, piece_selected),
                      'wK': Pawn(game.board, piece_coord, piece_selected),
                      'bP': Pawn(game.board, piece_coord, piece_selected),
                      'bR': Pawn(game.board, piece_coord, piece_selected),
                      'bN': Pawn(game.board, piece_coord, piece_selected),
                      'bB': Pawn(game.board, piece_coord, piece_selected),
                      'bQ': Pawn(game.board, piece_coord, piece_selected),
                      'bK': Pawn(game.board, piece_coord, piece_selected),
                      }