from .constants import N, S, W, E
WHITE_PAWN_STARTING_TILE = 6
BLACK_PAWN_STARTING_TILE = 1


class Piece:
    __init__(self, piece_selected, piece_coord)
        self.piece = piece_selected[1]
        self.piece_color = piece_selected[0]
        self.piece_coord = piece_coord

class Pawn(Piece):
    __init__(self, board):
        self.board = board

    def building_pawn_moves_list(self):
        if self.color == 'w':
            pawn_moves = [N]
            if self.coord[1] == WHITE_PAWN_STARTING_TILE: # Jezeli pionek jest na polu startowym
                pawn_moves.extend(adding_directions(N,N))
            if self.board(adding_directions(self.board.coord, (adding_directions(N,W))) == 'b':### DO POPRAWY
                pawn_moves.extend(adding_directions(N,W))
            if self.coord + (UP + RIGHT) == black
                pawn_moves.extend(adding_directions(N,E))
        elif self.color == 'b':
            pawn_moves = [S]
            if self.coord[1] == BLACK_PAWN_STARTING_TILE: # Jezeli pionek jest na polu startowym
                pawn_moves = extend(UPx2)
            if boord.coord + (UP + LEFT) == black
                pawn_moves = extend(UP + LEFT)
            if boord.coord + (UP + RIGHT) == black
                pawn_moves = extend(UP + RIGHT)


MOVEMENT ={
    'wP': (UP, (0, -2)),
    'wR': (UP, RIGHT, LEFT, DOWN),
    'wB': UP,
    'wN': UP,
    'wQ': UP,
    'wK': UP,
    'bP': (DOWN, (0, 2)),
    'bR': UP,
    'bN': UP,
    'bB': UP,
    'bQ': UP,
    'bK': UP,
}

ONLY_CAPTURING_MOVEMENT = {
    'wP':(UP+LEFT,UP+RIGHT),
    'bP':(DOWN+LEFT, DOWN+RIGHT)
}

# class Piece:
#     def __init__(self):
#         pass

def valid_pawn_moves(piece_selected, piece_coord, target_content, target_coord):  # move
    moves_allowed = []  # TU
    if piece_selected[0] == "w":  # JEZELI JEST BIALY
        if piece_coord[1] < 6:  # JEZELI NIE JEST TO JEGO PIERWSZY RUCH
            if target_content[0] == '-':  # JEZELI POLE DOCELOWE JEST PUSTE
                moves_allowed = MOVEMENT['wP']
                return moves_allowed
            else:  # JEZELI POLE DOCELOWE JEST ZAJETE
                moves_allowed = ONLY_CAPTURING_MOVEMENT['wP']
                return moves_allowed
        elif piece_coord[1] == 6:  # JEZELI JEST TO PIERWSZY RUCH TEJ BIERKI
            if target_content[0] == '-':
                print(MOVEMENT['wP'])
                moves_allowed = tuple(MOVEMENT['wP'])
                return moves_allowed
            else:
                moves_allowed = ONLY_CAPTURING_MOVEMENT['wP']
                return moves_allowed
        elif target_coord[1] == 0:
            if target_content[0] != '-':
                moves_allowed = MOVEMENT['wP']
                return moves_allowed  # promocja
            else:
                moves_allowed = ONLY_CAPTURING_MOVEMENT['wP']  # promocja
                return moves_allowed
    elif piece_selected[0] is "b":  # JEZELI CZARNY
        if piece_coord[1] > 1:  # JEZELI NIE JEST TO JEGO PIERWSZY RUCH
            if target_content[0] == '--':  # JEZELI POLE DOCELOWE JEST PUSTE
                moves_allowed = MOVEMENT['bP']
                return moves_allowed
            else:  # JEZELI POLE DOCELOWE JEST ZAJETE
                moves_allowed = ONLY_CAPTURING_MOVEMENT['bP']
                return moves_allowed
        elif piece_coord[1] == 1:  # JEZELI JEST TO PIERWSZY RUCH TEJ BIERKI
            if target_content[0] == '-':
                moves_allowed = (MOVEMENT['bP'])
                return moves_allowed
            else:
                moves_allowed = ONLY_CAPTURING_MOVEMENT['bP']
                return moves_allowed
        elif target_coord[1] == 7:
            if target_content[0] != '-':
                moves_allowed = MOVEMENT['bP']
                return moves_allowed  # promocja
            else:
                moves_allowed = ONLY_CAPTURING_MOVEMENT['bP']  # promocja
                return moves_allowed
        pass

        # self.wK = (DIRECTIONS.values())
            # castling = (2,0)(1,0)

        
        # if piece = king
        #     long_castling_flag = False
        #     short_castling_flag = False

        #     long_castling_flag = True
        #     short_castling_flag = True

        #     def castling ():
        #         if move == (2,0):
        #             board(7,7) = '--'
        #             board(6,7) = self.king()
        #             board(5,7) = self.rook()
        #             rook = (king.coord[0]-1)
        #         else:
        #             board(0,7) = '--'
        #             board(2,7) = self.king()

        # self.knight_moves():
        #     if abs(move)==3 
        #         pass
        #     else:
        #         pass
        #     # moves_list (1,2) (-1,2) (1,-2)(-1,-2) (-2, 1)(-2,-1) (2, 1) (2, -1)
        # self.bishop()# NIEDOROBIONE
        #     if sum(coord) % 2 != 0 :
        #         if move [row] == move [col] or sum(move) == sum(coord)
        #         return moves_allowed
        #     else:
        #         if move [row] == move [col] or sum(move) == sum(coord)
            
        # self.rook ()
        #     if (abs(0,move[1])) or (abs(move[0],0)):
        #         pass 
        # self.queen()
        #     self.rook()
        #     self.bishop()
        # self.king()
        #     self.queen
        # pass
