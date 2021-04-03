import pygame, os
from chess.constants import *
from chess.chessboard import Chessboard

pygame.init()
#IMPORTS
Chess = Chessboard()


#SETTINGS
FPS = 25
WIDTH, HEIGHT = 1400, 950
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Szachy')

def drawing_board():
    # DRAWING BOARD
    WINDOW.fill(PINK)
    BOARD_WHITE_BG = pygame.transform.scale(pygame.image.load(
        os.path.join('F:\projekty\Szachy VS\Images','white_tiles.jpg')),
        (B_BACKGROUND_WIDTH, B_BACKGROUND_HEIGHT))
    WINDOW.blit(BOARD_WHITE_BG, (BOARD_BACKGROUND_POSITION))
    for i in range (TILES_LENGHT):
        for j in range(TILES_LENGHT):
            if (i+j)%2 != 0:
                pygame.draw.rect(WINDOW, BROWN,(
                                (TILE_SIZE*i)+BOARD_POSITION[0],
                                (TILE_SIZE*j)+BOARD_POSITION[1],
                                 TILE_SIZE, TILE_SIZE))
    pygame.display.update()

def drawing_pieces():
    for col in range (TILES_LENGHT):
        for row in range (TILES_LENGHT):
            if Chess.board[col][row] != "--":
                tile = str(Chess.board[col][row])
                name = GRAPHICS_NAMES[tile]
                piece = pygame.transform.scale(pygame.image.load(
                    os.path.join('F:\projekty\Szachy VS\Images', name+'.png')),
                    (TILE_SIZE, TILE_SIZE))
                WINDOW.blit(piece,(BOARD_POSITION[0]+(TILE_SIZE*row), BOARD_POSITION[1]+(TILE_SIZE*col)))
    pygame.display.update()

# def update_board_view()
#     tile = str(Chess.board[x][y])
def get_game_coord_from_mouse():
    mouse_pos = pygame.mouse.get_pos()
    coord = ((mouse_pos[0] - BOARD_POSITION[1])//TILE_SIZE, (mouse_pos[1] - BOARD_POSITION[0])//TILE_SIZE)
    if BOARD_END_POSITION >= mouse_pos >= BOARD_POSITION:
        print("coord", coord)
        return coord


def selecting_tile(coord):
    # while piece == None and pygame.mouse.get_pressed()[0]:
    #     print("wybierz")       
    row, col = coord[0], coord[1]
    piece = Chess.board[col][row]# [ROW][COL]
    print("piece", piece)
    if piece == "--":
        print("nie mozna zaznaczyc --")
        get_game_coord_from_mouse()
    else:
        print('robi return ',piece)
        return piece

def making_move(piece_selected, base_coord, coord):
    target_coord = coord
    row, col = target_coord[0], target_coord[1]
    target_content = Chess.board[col][row]
    print(piece_selected,'x', base_coord,'x', target_content,'x', target_coord)
    if target_content == "--":
        Chess.board[base_coord[1]][base_coord[0]] = "--" 
        Chess.board[target_coord[1]][target_coord[0]] = piece_selected
        print("valid_base", Chess.board[base_coord[0]][base_coord[1]])
        print("valid_target", Chess.board[target_coord[1]][target_coord[0]])
        drawing_pieces()   
   
def clear_clicks():
    return None

def main():
    tester = 1
    clock = pygame.time.Clock()
    piece_selected = None
    run = True
    drawing_board()
    drawing_pieces()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:# jezeli wcisniety LEFT MOUSE BUTTON
                # mouse_pos = pygame.mouse.get_pos()
                # get_game_coord_from_mouse():
                # print(tester,"tester")
                # tester+=1     
                coord = get_game_coord_from_mouse()
                if piece_selected == None and coord != None:
                    piece_selected = selecting_tile(coord)
                    if piece_selected == '--':
                        piece_selected = None
                        break
                    coord_selected = coord
                elif piece_selected != "--" and piece_selected != None and coord != None:
                    making_move(piece_selected, coord_selected, coord)
                    piece_selected = clear_clicks()
                    print("wykonano ruch i wyczyszczono")
                # if selecting_tile() != None:
                #     # piece_selected, coord_selected = selecting_tile()
                #     print(piece_selected, coord_selected)
                
        # if pygame.mouse.get_pressed()[0] and BOARD_END_POSITION >= mouse_pos >= BOARD_POSITION:        
        # if piece_selected  == None:# PYTA O ZAZNACZONE POLE DOPOKI ZAZNACZONE POLE NIE BEDZIE ZAWIERAC FIGURY
        # piece_selected, coord_selected = selecting_tile()
        #     print ("Zaznaczone pole", piece_selected, coord_selected)           
        # print ("piece_selected nie jest --, wykonuje making_move")




    pygame.quit()

if __name__ == "__main__":
   main()



