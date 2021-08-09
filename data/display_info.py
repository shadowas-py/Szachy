def translate_to_chess_notation(*args, track = False):
    y_coord_dict = {0: '8', 1: '7', 2: '6', 3: '5', 4: '4', 5: '3', 6: '2', 7: '1'}
    x_coord_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
    for arg in args:
        print(x_coord_dict[arg[0]], y_coord_dict[arg[1]], sep='', end='')
        arg = arg[2:]
        if arg:
            translate_to_chess_notation(arg)
        else:
            print ('._.', end='')


if __name__ == '__main__':
    translate_to_chess_notation((0,0, 1,7),(5,5),(1,1),(3,4))





