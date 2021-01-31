
import aoc.utils
import itertools

data = aoc.utils.read_files('d3')
#data = aoc.utils.read_files('d3', fname='example.txt')
line_length = len(data[0])

def check_slope(right, down):
    right_pos = 0
    num_trees = 0

    # Skip first line, first move goes down
    for ind, line in enumerate(data[1:], start=1):
        if ind % down != 0:
            continue
        right_pos += right
        
        pos = line[right_pos % line_length]
        if pos == '#':
            num_trees += 1

    return num_trees

slopes = (
    check_slope(1, 1),
    check_slope(3, 1),
    check_slope(5, 1),
    check_slope(7, 1),
    check_slope(1, 2)
)
slope_product = 1
for s in slopes:
    slope_product *= s
print(slope_product)
