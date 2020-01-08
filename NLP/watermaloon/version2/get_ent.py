from math import log


def get_ent(p):
    if (p == 0):
        part1 = 0
        part2 = 0
    elif (p == 1):
        part1 = 0
        part2 = 0
    else:
        part1 = p * log(p, 2)
        part2 = (1 - p) * log((1 - p), 2)
    return -1 * (part1 + part2)
