class Player:

    def __init__(self, color):
        self.color = color
        self.time = ...

        self.pieces = ...

        self.pins = {}  # pinned_tile: all tiles between attacker and enemy king
        self.checks = {}
        self.attacked_tiles_in_check = {}

        self.all_attacked_tiles = []
        self.all_possible_moves = []

    def clear_checks_and_pins(self):
        self.pins.clear(); self.checks.clear(); self.attacked_tiles_in_check.clear(); self.all_possible_moves.clear()








