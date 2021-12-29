import heapq

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

original_data = [[int(num) for num in line] for line in RAW.splitlines()]
tile_w = len(original_data)
tile_h = len(original_data[0])


def tesselate(nums: list[list[int]]) -> list[list[int]]:
    """Tile downward and upward, each time the tile repeats to the right or downward,
    all of its risk levels are 1 higher than the tile immediately up or left of it
    """
    for _ in range(4):
        for row in nums:
            last = row[-tile_w:]
            row.extend((x + 1) if x < 9 else 1 for x in last)

    for _ in range(4):
        for row in nums[-tile_h:]:
            nums.append([(x + 1) if x < 9 else 1 for x in row])
    return nums


def get_neighbours(x: int, y: int) -> list[tuple[int, int]]:
    possible_neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    neighbours = []
    for n in possible_neighbours:
        x_, y_ = n
        if x_ < 0 or y_ < 0 or x_ == len(data) or y_ == len(data):
            continue
        neighbours.append(n)
    return neighbours


data = tesselate(original_data)


if __name__ == "__main__":
    visited: dict[tuple[int, int] : bool] = {
        (i, j): False for i in range(len(data)) for j in range(len(data[0]))
    }
    # use None for infinity
    distances = [[float("inf") for _ in num_line] for num_line in data]
    distances[0][0] = 0

    queue = []
    heapq.heappush(queue, (0, (0, 0)))
    while len(queue) > 0:
        current_val, current = heapq.heappop(queue)
        for n in get_neighbours(*current):
            if visited[n]:
                continue

            n_val = current_val + data[n[0]][n[1]]
            if n_val < distances[n[0]][n[1]]:
                distances[n[0]][n[1]] = n_val
                heapq.heappush(queue, (n_val, (n[0], n[1])))
        visited[current] = True

    print(distances[len(data) - 1][len(data[0]) - 1])

    # not 2663...
