def get_input():
    with open("input_3.txt") as f:
        raw = f.read()
    return raw.splitlines()


def part_1():
    counts = {ind: 0 for ind in range(12)}

    for line in data:
        for ind, char in enumerate(line):
            counts[ind] += int(char)
    # print(counts)
    # manually read through these
    gamma = "001110100111"
    epsilon = "110001011000"

    power = int(gamma, 2) * int(epsilon, 2)


## PART 2


def count_ind(data: list[str], ind: int) -> int:
    """Count all the values at an index"""
    return [int(line[ind]) for line in data]


def part_2():
    data = get_input()
    #     data = """00100
    # 11110
    # 10110
    # 10111
    # 10101
    # 01111
    # 00111
    # 11100
    # 10000
    # 11001
    # 00010
    # 01010""".splitlines()

    ind = 0
    while len(data) > 1:
        ones = sum(int(line[ind]) for line in data)
        if ones >= len(data) / 2:
            most_common_val = "1"
        else:
            most_common_val = "0"
        data = [line for line in data if line[ind] != most_common_val]
        ind += 1
        ind %= len(data[0])
        print(f"{data=}")
    print(f"Num: {data[0]}, decimal: {int(data[0], 2)}")


part_2()
