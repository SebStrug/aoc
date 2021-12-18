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


def get_adjacent_vals(nums: list[list[int]], x: int, y: int) -> list[tuple[int, int]]:
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
            if (x_ == len(nums[0])) or (y_ == len(nums)):
                continue
            adjacent.append(nums[x_][y_])
    return adjacent


def get_low_points():
    low_points = []
    for col_ind in range(len(nums)):
        for row_ind in range(len(nums[0])):
            adjacent_points = get_adjacent_vals(nums, row_ind, col_ind)
            if all(nums[row_ind][col_ind] < adj for adj in adjacent_points):
                low_points.append(nums[row_ind][col_ind])
    return low_points


low_points = get_low_points()
print(low_points)
print(sum(1 + point for point in low_points))
