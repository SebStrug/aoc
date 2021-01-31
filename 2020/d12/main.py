import math
from utils import read_files

raw = read_files('d12')

# x, y plane where x is east, -x is west
# -y is south, y is north

facing = [1, 0]  # start facing east
loc = [0, 0]

facing_poss = [[1, 0], [0, -1], [-1, 0], [0, 1]]

for line in raw:
    action = line[0]
    val = int(line[1:])

    if action == 'N':
        loc[1] += val
    elif action == 'S':
        loc[1] -= val
    elif action == 'E':
        loc[0] += val
    elif action == 'W':
        loc[0] -= val

    elif action == 'R':  # rotate clockwise
        facing = facing_poss[int((facing_poss.index(facing) + (val / 90)) % 4)]
    elif action == 'L':  # rotate counterclockwise
        facing = facing_poss[int((facing_poss.index(facing) - (val / 90)) % 4)]

    elif action == 'F':
        loc[0] += facing[0] * val
        loc[1] += facing[1] * val

# problem 1
#print(abs(loc[0]) + abs(loc[1]))


def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


waypoint = [10, 1]
loc = [0, 0]

for line in raw:
    action = line[0]
    val = int(line[1:])

    if action == 'N':
        waypoint[1] += val
    elif action == 'S':
        waypoint[1] -= val
    elif action == 'E':
        waypoint[0] += val
    elif action == 'W':
        waypoint[0] -= val

    elif action == 'R':  # rotate clockwise
        way_x, way_y = rotate(loc, waypoint, math.radians(-val))
        waypoint = [way_x, way_y]
    elif action == 'L':  # rotate counterclockwise
        way_x, way_y = rotate(loc, waypoint, math.radians(val))
        waypoint = [way_x, way_y]

    elif action == 'F':
        rel_x = waypoint[0] - loc[0]
        rel_y = waypoint[1] - loc[1]
        loc[0] += rel_x * val
        loc[1] += rel_y * val
        # waypoint stays in same pos relative to ship
        waypoint[0] = loc[0] + rel_x
        waypoint[1] = loc[1] + rel_y
    print(line, loc, waypoint)

print(abs(loc[0]) + abs(loc[1]))
