import pygame
from data.constants import *
from data.chessboard import Game
from data.settings import *
from data.game_logic import *
from data.graphic import *

pygame.init()

#IMPORTS
game = Game()
# graphic = Graphic()

#SETTINGS
pygame.display.set_caption('Szachy')

def get_game_coord_from_mouse():
    mouse_pos = pygame.mouse.get_pos()
    coord = ((mouse_pos[0] - BOARD_POSITION[1])//TILE_SIZE, (mouse_pos[1] - BOARD_POSITION[0])//TILE_SIZE)
    if BOARD_END_POSITION >= mouse_pos >= BOARD_POSITION:
        return coord


def selecting_tile(coord):  
    row, col = coord[0], coord[1]
    piece = game.board[col][row]
    if piece == "--":
        get_game_coord_from_mouse()
    else:
        return piece

def making_move(piece_selected, base_coord, target_coord):
    row, col = target_coord[0], target_coord[1]
    target_content = game.board[col][row]
    if target_content == "--":
        game.board[base_coord[1]][base_coord[0]] = "--" 
        game.board[target_coord[1]][target_coord[0]] = piece_selected
        for i in range (len(game.board)):
            print(game.board[i])
        print("\n")
   
def clear_click():
    return None

def main():
    clock = pygame.time.Clock()
    piece_selected = None
    run = True
    drawing_board()
    drawing_pieces(game.board)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:# jezeli wcisniety LEFT MOUSE BUTTON
                coord = get_game_coord_from_mouse()
                if piece_selected == None and coord != None:
                    piece_selected = selecting_tile(coord)
                    if piece_selected == '--':
                        piece_selected = None
                        break
                    coord_selected = coord
                elif piece_selected != "--" and piece_selected != None and coord != None:
                    making_move(piece_selected, coord_selected, target_coord=coord)
                    drawing_pieces(game.board)   
                    piece_selected = clear_click()
                    pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
   main()


#Zrobic porzadek
#przezroczystosc pol
# zrobic poprawne poprawnie grafike z odswiezaniem
#1.Zrobic tury
#2.Zrobić poruszanie się figur
#3.Zrobic bicie
#4.Promocja piona