from typing import Optional

RAW_TEST = """2199943210
3987894921
9856789892
8767896789
9899965678"""

with open("input_9.txt") as f:
    RAW = f.read()

data = RAW.splitlines()

nums = []
for line in data:
    num_line = [int(digit) for digit in line]
    nums.append(num_line)


def get_adjacent(nums: list[list[int]], x: int, y: int) -> list[tuple[int, int]]:
    """Get the points adjacent to a point, not wrapping around"""
    adjacent = []
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            # look at non-diagonals
            if not (i == 0 or j == 0):
                continue
            # skip the point itself
            if i == 0 and j == 0:
                continue

            x_ = x + i
            y_ = y + j
            # no negative indexing
            if (x_ < 0) or (y_ < 0):
                continue
            # not out of bounds
            if (x_ == len(nums)) or (y_ == len(nums[0])):
                continue
            adjacent.append((x_, y_))
    return adjacent


def get_low_point_inds() -> list[tuple[int, int]]:
    """Get the indices of the lowest points in the grid"""
    low_points = []
    for col_ind in range(len(nums[0])):
        for row_ind in range(len(nums)):
            adjacent_point_inds = get_adjacent(nums, row_ind, col_ind)
            adjacent_points = [nums[adj[0]][adj[1]] for adj in adjacent_point_inds]
            if all(nums[row_ind][col_ind] < adj for adj in adjacent_points):
                low_points.append((row_ind, col_ind))
    return low_points


low_points = get_low_point_inds()

# for each low point
# get adjacent points
# add any adjacent points not equal to 9 to a visited list
# repeat for each adjacent point until visited list does not expand
# return the number of visited points


def get_basin_size(low_point: tuple[int, int]) -> int:
    visited = set()
    untried = set([low_point])

    while len(untried) > 0:
        point = untried.pop()
        visited.add(point)

        adjs = get_adjacent(nums, point[0], point[1])
        for adj in adjs:
            if nums[adj[0]][adj[1]] != 9 and adj not in visited:
                untried.add(adj)
    return len(visited)


basin_sizes = [get_basin_size(low_point) for low_point in low_points]
largest_basins = list(sorted(basin_sizes))[-3:]
print(largest_basins[0] * largest_basins[1] * largest_basins[2])
