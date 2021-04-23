# OBJECTS SIZES
BOARD_SIZE = 800
B_BACKGROUND_WIDTH = 900
B_BACKGROUND_HEIGHT = 900
GRID_SIZE = 8
TILE_SIZE = BOARD_SIZE // GRID_SIZE

# OBJECTS COORDINATES
BOARD_BACKGROUND_POSITION = (10, 10)
BOARD_POSITION = (60, 60)
BOARD_END_POSITION = (BOARD_POSITION[0] + BOARD_SIZE, BOARD_POSITION[1] + BOARD_SIZE)
# BOARD_x = 
# BOARD_y = 

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (50, 50, 50)
PINK = (240, 50, 210)
BROWN = (100, 50, 0)

# PIECES IMAGES
GRAPHICS_NAMES = {'wP': 'white_pawn',
                  'wR': 'white_rook',
                  'wN': 'white_knight',
                  'wB': 'white_bishop',
                  'wQ': 'white_queen',
                  'wK': 'white_king',
                  'bP': 'black_pawn',
                  'bR': 'black_rook',
                  'bN': 'black_knight',
                  'bB': 'black_bishop',
                  'bQ': 'black_queen',
                  'bK': 'black_king',
                  }
# DIRECTIONS
N = [0, -1]
S = [0, 1]
W = [-1, 0]
E = [1, 0]

# DIRS = {
#     'LEFT': (-1, 0),
#     'LEFT_UP': (-1, -1),
#     'UP': (0, -1),
#     'RIGHT_UP': (1, -1),
#     'RIGHT': (1, 0),
#     'RIGHT_DOWN': (1, 1),
#     'DOWN': (0, 1),
#     'LEFT_DOWN': (-1, 1)
# }
