from utils import read_files
from copy import deepcopy

raw = read_files('d11')
max_row = len(raw)
max_s = len(raw[0])

seat_pos = set()
for ind_row, row in enumerate(raw):
    for ind_s, s in enumerate(row):
        if s == 'L':
            seat_pos.add((ind_row, ind_s))


def show_seats(occupied_seats):
    all_lines = []
    for i in range(max_row):
        line = ''
        for j in range(max_s):
            if (i, j) in occupied_seats:
                line += '#'
            elif (i, j) in seat_pos:
                line += 'L'
            else:
                line += '.'
        all_lines.append(line)
    [print(i) for i in all_lines]
    print()


def get_adjacent_vals(seat) -> set:
    adj = []
    for r in (1, 0, -1):
        for s in (1, 0, -1):
            new_r = seat[0] + r
            new_s = seat[1] + s
            if (r == 0) and (s == 0):
                continue
            elif (new_r < 0 or new_r > max_row):
                continue
            elif (new_s < 0 or new_s > max_s):
                continue
            adj.append((seat[0]+r, seat[1]+s))
    return set(adj)


def loop(occupied_seats: set):
    new_occupied_seats = deepcopy(occupied_seats)
    # empty seats
    for seat in (seat_pos - occupied_seats):
        adj_vals = get_adjacent_vals(seat)
        if len(adj_vals.intersection(occupied_seats)) == 0:
            new_occupied_seats.add(seat)

    for seat in occupied_seats:
        adj_vals = get_adjacent_vals(seat)
        if len(adj_vals.intersection(occupied_seats)) >= 4:
            new_occupied_seats.remove(seat)
    return new_occupied_seats


# after one round, occupied seats are seat pos
occupied_seats = seat_pos
show_seats(occupied_seats)
while True:
    new_occupied_seats = loop(occupied_seats)
    if new_occupied_seats == occupied_seats:
        break
    occupied_seats = deepcopy(new_occupied_seats)
    # show_seats(new_occupied_seats)
print(len(occupied_seats))
