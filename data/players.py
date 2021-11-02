class Player:

    def __init__(self, color):
        self.color = color
        self.time = ...

        self.pieces = ...

        self.pins = {}  # pinned_tile: all tiles between attacker and enemy king
        self.checks = {}
        self.attacked_tiles_in_check = {}

        self.all_attacked_tiles = []
        self.all_possible_moves = ...








