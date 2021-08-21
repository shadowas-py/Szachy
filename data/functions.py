def sum_directions(direction1, direction2, direction3=(0, 0)):
    return tuple(map(sum, zip(direction1, direction2, direction3)))

def sub_directions(direction1, direction2):
    return tuple(nCoord1 - nCoord2 for nCoord1, nCoord2 in zip(direction1, direction2))

def multiply_direction(direction, multiplier):
    return tuple((direction[0] * multiplier, direction[1] * multiplier))

def shift_value(coord1, coord2):
    for i in range(2):
        yield coord1[i] - coord2[i] if coord1[i] >= coord2[i] else coord2[i] - coord1[i]

def midpoint_between_two_coords(coord1, coord2):
    for i in range(2):
        yield (coord1[i] + coord2[i])//2

def rotations(v):
    x, y = v
    return [(x,y), (y,-x), (-x,-y), (-y,x)]
