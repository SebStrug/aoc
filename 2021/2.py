with open("input_2.txt", "r") as f:
    raw = f.read()

lines = raw.split("\n")[:-1]

print(lines)

import re

horiz = 0
depth = 0
aim = 0
for line in lines:
    num = re.search(r"\d+", line).group()
    if "down" in line:
        aim += int(num)
    elif "forward" in line:
        horiz += int(num)
        depth += aim * int(num)
    elif "up" in line:
        aim -= int(num)

print(horiz * depth)

# not 3388260
