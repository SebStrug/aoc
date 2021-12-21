RAW_TEST = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###""".splitlines()

with open('input_20.txt', 'r') as f:
    RAW = f.read().splitlines()

enhance_line, *image = RAW_TEST
# skip blank line
image = image[1:]

def get_adj(x: int, y: int) -> list[str]:
    """Get the lines around a point from the image"""
    adj = []
    for i in (-1, 0, 1):
        line = ''
        for j in (-1, 0, 1):
            x_, y_ = x + i, y + j
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

def get_new_im(old_image: list[str], enhance_line: str) -> list[str]:
    num = get_bin(old_image)
    return [old_image[0], old_image[1][0] + str(enhance_line[num]) + old_image[1][2], old_image[2]]

# REPEAT x2:
# for each 3x3 box (from one inside the buffer...) get the adjacent
# keep adjacent and add to a new image
def enhance_image(image: list[str], enhance_line: str) -> list[str]:
    total = []
    for x in range(-1, len(image)+1):
        row = ''
        for y in range(-1, len(image[0])+1):
            adj_image = get_adj(x, y)
            new_image = get_new_im(adj_image, enhance_line)
            # only important value is middle
            row += new_image[1][1]
        total.append(row)
    return total

for _ in range(2):
    image = enhance_image(image, enhance_line)
    for line in image:
        print(line)
    print()

num_lit = 0
for line in image:
    for char in line:
        if char == '#':
            num_lit += 1

print(num_lit)
# NOT 5481 or 6520, both too high

# something to do with first pixel being a # so this creates a border of #?