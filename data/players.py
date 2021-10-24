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
    absolute_pins = {} # attacker: defender
    pinned_tiles = {} # attacker: all tiles between attacker and enemy king

    def __init__(self, color):
        self.color = color
        self.time = ...






