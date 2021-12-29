RAW_TEST = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""

RAW_TEST_1 = """..........
.>v....v..
.......>..
.........."""

with open("input_25.txt", "r") as f:
    RAW = f.read()

data = [[c for c in line] for line in RAW.splitlines()]


def step_east(data_: list[list[str]]) -> list[list[str]]:
    new: list[tuple[int, int]] = []
    for row in range(len(data_)):
        for col in range(len(data_[0])):
            if data_[row][col] == ".":
                continue
            elif data_[row][col] == ">":
                col_ = col + 1
                if col_ == len(data_[0]):
                    col_ = 0

                if data_[row][col_] != ".":
                    new.append((row, col))
                else:
                    new.append((row, col_))

    new_data = [[c if c != ">" else "." for c in line] for line in data_]
    for v in new:
        new_data[v[0]][v[1]] = ">"
    return new_data


def step_south(data_: list[list[str]]) -> list[list[str]]:
    new: list[tuple[int, int]] = []
    for row in range(len(data_)):
        for col in range(len(data_[0])):
            if data_[row][col] == ".":
                continue
            elif data_[row][col] == "v":
                row_ = row + 1
                if row_ == len(data_):
                    row_ = 0

                if data_[row_][col] != ".":
                    new.append((row, col))
                else:
                    new.append((row_, col))

    new_data = [[c if c != "v" else "." for c in line] for line in data_]
    for v in new:
        new_data[v[0]][v[1]] = "v"
    return new_data


def step(data_: list[list[str]]) -> list[list[str]]:
    east_data = step_east(data_)
    return step_south(east_data)


count = 0
new_data = []
while True:
    new_data = step(data)
    count += 1
    if new_data == data:
        break
    else:
        data = new_data
    if count > 10_000:
        break
print(count)

# def show(data):
#     for l in data:
#         print(l)
#     print()

# show(data)
# data = step(data)
# show(data)
