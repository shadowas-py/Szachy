def sum_directions(direction1, direction2, direction3=(0, 0)):
    return tuple(map(sum, zip(direction1, direction2, direction3)))


def sub_directions(direction1, direction2):
    return tuple(nCoord1 - nCoord2 for nCoord1, nCoord2 in zip(direction1, direction2))


def multiply_direction(direction, multiplier):
    return tuple((direction[0] * multiplier, direction[1] * multiplier))


def rotations(v):
    x, y = v
    return [(x,y), (y,-x), (-x,-y), (-y,x)]
