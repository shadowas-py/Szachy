from data.constants import GRID_SIZE

class Player:
    def pieces_list(self, game):
        for col in range(GRID_SIZE):
            for row in range(GRID_SIZE):
                if game.board[row][col] and game.board[row][col].color == self.color:
                    yield game.board[row][col]

    def __init__(self, color):
        self.id = self.__hash__()
        self.color = color
        self.time = ...

        self.pieces = self.pieces_list

        self.pins = {}  # pinned_tile: all tiles between attacker and enemy king
        self.checks = {}
        self.attacked_tiles_in_check = {}

        self.all_attacked_tiles = []
        self.all_possible_moves = []

    def __str__(self):
        return self.color+' ... '+ str(self.id)

    def clear_checks_and_pins(self):
        self.pins.clear(); self.checks.clear(); self.attacked_tiles_in_check.clear(); self.all_possible_moves.clear()
