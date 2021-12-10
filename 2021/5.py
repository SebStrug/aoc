with open("input_5.txt", "r") as f:
    RAW = f.readlines()

RAW_TEST = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split(
    "\n"
)

coords = []
for line in RAW:
    line = line.strip()
    coords_1, coords_2 = line.split(" -> ")
    x_1, y_1 = map(int, coords_1.split(","))
    x_2, y_2 = map(int, coords_2.split(","))
    coord = tuple(map(int, (x_1, y_1, x_2, y_2)))
    # Horizontals and verticals
    if x_1 == x_2 or y_1 == y_2:
        coords.append(coord)
    # Diagonals
    elif x_1 == y_1 and x_2 == y_2:
        coords.append(coord)
    elif abs(x_1 - x_2) == abs(y_1 - y_2):
        coords.append(coord)

from collections import defaultdict

cov_points = defaultdict(int)


def my_range(a, b):
    """Do a reverse range if a > b, handle ending points"""
    if a > b:
        return range(b, a + 1)
    return range(a, b + 1)


def get_diag_range(x_1, y_1, x_2, y_2):
    """Handle diagaonls where (x_1 == y_2 and x_2 == y_1) or (x_2 == y_1 and x_1 == y_2)"""
    while (x_1, y_1) != (x_2, y_2):
        yield (x_1, y_1)
        if x_1 < x_2:
            x_1 += 1
        else:
            x_1 -= 1
        if y_1 < y_2:
            y_1 += 1
        else:
            y_1 -= 1
    yield (x_1, y_1)


for c in coords:
    x_1, y_1, x_2, y_2 = c
    # Handle horizontal
    if x_1 == x_2 and y_1 != y_2:
        print(f"Horizontal: {c}")
        for y in my_range(y_1, y_2):
            cov_points[(x_1, y)] += 1
    # Handle vertical
    elif y_1 == y_2 and x_1 != x_2:
        print(f"Vertical: {c}")
        for x in my_range(x_1, x_2):
            cov_points[(x, y_1)] += 1

    # Handle diagonals
    elif x_1 == y_1 and x_2 == y_2:
        print(f"Eq Diagonals: {c}, {x_1=}, {y_1=}, {x_2=}, {y_2=}")
        for p in get_diag_range(x_1, y_1, x_2, y_2):
            cov_points[p] += 1
            print(p)
    elif abs(x_1 - x_2) == abs(y_1 - y_2):
        print(f"Diagonals: {c}")
        for p in get_diag_range(x_1, y_1, x_2, y_2):
            cov_points[p] += 1
            print(p)
    else:
        print(f"No fit: {c}")

print(dict(filter(lambda x: x[1] > 1, cov_points.items())))
print(sum(1 for _, v in cov_points.items() if v > 1))
