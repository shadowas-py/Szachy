# FUNKCJA DO PROWADZENIA ZAPISU PARTII

coordMap = lambda it: chr(65 + it[0]) + str(8 - it[1])


def translate_to_chess_notation(*movesLists):
    print('MOŻLIWE RUCHY NA POLA:')
    for movesList in movesLists:
        print(' '.join(
            map(lambda it: coordMap(it[0]) + ">>" + coordMap(it[1]) if type(it[0]) is tuple else coordMap(it),
                movesList)))
    # IZ: Twoja funkcja powinna na końcu printować nową linię. inaczej następny print zacznie pisać od tej samej!


if __name__ == '__main__':
    # translate_to_chess_notation((0,0, 1,7),(5,5),(1,1),(3,4))
    translate_to_chess_notation([(2, 7), ((0, 7), (3, 7)), (6, 7), ((7, 7), (5, 7)), (5, 7), (3, 7)])
