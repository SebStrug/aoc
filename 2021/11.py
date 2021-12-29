from typing import Optional

RAW_TEST = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

with open("input_11.txt", "r") as f:
    RAW = f.read()

data = RAW.splitlines()

nums: list[list[int]] = []
for line in data:
    num_line = []
    for char in line:
        num_line.append(int(char))
    nums.append(num_line)


def incr_energies(nums: list[list[int]]) -> list[list[int]]:
    return [[num + 1 for num in num_line] for num_line in nums]


def get_adj(x: int, y: int) -> list[tuple[int, int]]:
    adjs = []
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            # ignore the current point
            if i == 0 and j == 0:
                continue
            x_ = x + i
            y_ = y + j
            # no negative indexing
            if x_ < 0 or y_ < 0:
                continue
            # don't go out of bounds
            if x_ == len(nums) or y_ == len(nums):
                continue
            adjs.append((x_, y_))
    return adjs


def get_flasher(
    nums: list[list[int]], has_flashed: set[tuple[int, int]]
) -> Optional[tuple[int, int]]:
    for row in range(len(nums)):
        for col in range(len(nums[row])):
            if nums[row][col] > 9 and (row, col) not in has_flashed:
                return (row, col)
    return None


def step(nums: list[list[int]]) -> tuple[list[list[int]], int]:
    nums = incr_energies(nums)

    has_flashed: set[tuple[int, int]] = set()
    while True:
        flasher = get_flasher(nums, has_flashed)
        if not flasher:
            break

        has_flashed.add(flasher)
        adjacents = get_adj(flasher[0], flasher[1])
        for adj in adjacents:
            if adj not in has_flashed:
                nums[adj[0]][adj[1]] += 1

    for point in has_flashed:
        nums[point[0]][point[1]] = 0
    return nums, len(has_flashed)


total_flashes = 0
for step_num in range(100):
    nums, num_flashes = step(nums)
    total_flashes += num_flashes
print(total_flashes)
