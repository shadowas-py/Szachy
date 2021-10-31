from data.constants import GRID_SIZE
# players_color_list = ['w','b']
#
# def setting_instances_global_names(cls, how_many, *args):
#     cls.id_counter = 1
#
#     def instance_name(cls):
#         return 'player'+(str(cls.id_counter))
#
#     for i in range(0, how_many):
#         globals()[instance_name(cls)] = cls(args[i])
#         cls.id_counter += 1
# setting_instances_global_names(Player,len(players_color_list),*players_color_list)

class Player:

    def __init__(self, color):
        self.color = color
        self.time = ...
        self.pins = {}  # attacker: defender
        self.attacked_tiles_in_pin = {}  # attacker: all tiles between attacker and enemy king
        self.checks = {}
        self.attacked_tiles_in_check = {}
        self.all_attacked_tiles = []
        self.all_possible_possible_moves = ...

    def pieces_list(self, game):
        for col in range(GRID_SIZE):
            for row in range(GRID_SIZE):
                if game.board[row][col] and game.board[row][col].color == self.color:
                    yield game.board[row][col]

