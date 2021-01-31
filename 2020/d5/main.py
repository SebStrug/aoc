from utils import read_files
import re

raw = read_files('d5') #, 'example.txt')

def get_row(seat: str) -> int:
    """Get the seat row"""
    binary_str = ''
    chars = seat[:7]
    for char in chars:
        if char == 'F':
            binary_str += '0'
        elif char == 'B':
            binary_str += '1'
        else:
            raise ValueError(f'Error with seat: {chars}')
    return int(binary_str, 2)

def get_column(seat: str) -> int:
    """Get the column row"""
    binary_str = ''
    chars = seat[7:]
    for char in chars:
        if char == 'L':
            binary_str += '0'
        elif char == 'R':
            binary_str += '1'
        else:
            raise ValueError(f'Error with seat: {chars}')
    return int(binary_str, 2) 

def get_seat_id(row: int, column: int) -> int:
    return (row * 8) + column

# part 1
max_seat_id = 0
for seat in raw:
    row = get_row(seat)
    column = get_column(seat)
    seat_id = get_seat_id(row, column)
    if seat_id > max_seat_id:
        max_seat_id = seat_id
print(max_seat_id)

# part 2
all_seat_ids = [get_seat_id(get_row(s), get_column(s)) for s in raw]
print([x for x in range(min(all_seat_ids), max(all_seat_ids) + 1) if x not in all_seat_ids])