from aoc import *

data = ints(read_lines(1))

def first():
    incr = 0
    for ind, num in enumerate(data):
        if ind == 0:
            continue
        if num > data[ind - 1]:
            incr += 1

    print(incr)

incr = 0
prev_window = 0
for ind, num in enumerate(data):
    try:
        window = num + data[ind+1] + data[ind+2]
    except IndexError:
        break

    if ind == 0:
        prev_window = window
        continue
    if window > prev_window:
        incr += 1
    prev_window = window

print(incr)