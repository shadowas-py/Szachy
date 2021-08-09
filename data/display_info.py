# FUNKCJA DO PROWADZENIA ZAPISU PARTII

def translate_to_chess_notation(*args, trace = False):
    y_coord_dict = {0: '8', 1: '7', 2: '6', 3: '5', 4: '4', 5: '3', 6: '2', 7: '1'}
    x_coord_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
    print('MOZLIWE RUCHY NA POLA:')
    for arg in args:
        for coord in arg:
            try:
                print(x_coord_dict[coord[0]], y_coord_dict[coord[1]], sep='', end=' ')
            except KeyError:
                print(x_coord_dict[coord[0][0]], y_coord_dict[coord[0][1]], sep='', end='>>')
                print(x_coord_dict[coord[1][0]], y_coord_dict[coord[1][1]],sep='', end=' ')


if __name__ == '__main__':
    # translate_to_chess_notation((0,0, 1,7),(5,5),(1,1),(3,4))
    translate_to_chess_notation([(2, 7), ((0, 7), (3, 7)), (6, 7), ((7, 7), (5, 7)), (5, 7), (3, 7)])
