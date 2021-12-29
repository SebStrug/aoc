RAW_TEST = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""

with open("input_15.txt", "r") as f:
    RAW = f.read()

data = [[int(num) for num in line] for line in RAW.splitlines()]


def get_neighbours(x: int, y: int) -> list[tuple[int, int]]:
    possible_neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    neighbours = []
    for n in possible_neighbours:
        x_, y_ = n
        if x_ < 0 or y_ < 0 or x_ == len(data) or y_ == len(data):
            continue
        neighbours.append(n)
    return neighbours


def get_smallest(
    distances: list[list[int]], unvisited: set[tuple[int, int]]
) -> tuple[tuple[int, int], int]:
    """Return (distance indices, distance) of unvisited node with smallest distance"""
    d = {inds: distances[inds[0]][inds[1]] for inds in unvisited}
    return list(sorted(d.items(), key=lambda x: x[1]))[0]


unvisited: set[tuple[int, int]] = {
    (i, j) for i in range(len(data)) for j in range(len(data[0]))
}
# use None for infinity
distances = [[float("inf") for _ in num_line] for num_line in data]
distances[0][0] = 0

current = (0, 0)
current_val = 0
while True:
    neighbours = get_neighbours(*current)
    for n in neighbours:
        if n not in unvisited:
            continue

        n_val = current_val + data[n[0]][n[1]]
        n_distance = distances[n[0]][n[1]]
        if n_val < n_distance:
            distances[n[0]][n[1]] = n_val
    unvisited.remove(current)

    if len(unvisited) == 0:
        break
    current, current_val = get_smallest(distances, unvisited)

print(distances)


# NOT 699
