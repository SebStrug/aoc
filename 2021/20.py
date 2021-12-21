RAW_TEST = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###""".splitlines()

with open('input_20.txt', 'r') as f:
    RAW = f.read().splitlines()

enhance, *image = RAW_TEST
# skip blank line
image = image[1:]

def get_adj(current: tuple[int, int]) -> list[str]:
    """Get the lines around a point from the image"""
    adj = []
    for i in (-1, 0, 1):
        line = ''
        for j in (-1, 0, 1):
            x_, y_ = current[0] + i, current[1] + j
            if x_ < 0 or y_ < 0:
                line += '.'
            elif x_ >= len(image) or y_ >= len(image[0]):
                line += '.'
            else:
                line += image[x_][y_]
        adj.append(line)
    return adj

def get_bin(im_part: list[str]) -> int:
    """Convert a 3x3 image into a binary number then to decimal"""
    num = ''
    for line in im_part:
        for char in line:
            num += '0' if char == '.' else '1'
    return int(num, 2)


# REPEAT x2:
# for each 3x3 box (from one inside the buffer...) get the adjacent
# keep adjacent and add to a new image
adj_images = []
for point in range(-1, len(image)):
    adj_image = get_adj((point, point))
    num = get_bin(adj_image)
    adj_image[1] = f'{adj_image[1][0]}{enhance[num]}{adj_image[1][2]}'
    adj_images.append(adj_image)
