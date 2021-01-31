from itertools import product
from utils import read_files
import re
from typing import List

raw = read_files('d14')
mask_mem_in = read_files('d14', fname='example.txt')


def get_bin_string(num: int) -> str:
    """Get 36bit binary string representation of decimal num"""
    return str(bin(num)).replace('0b', '').rjust(36, '0')


def apply_mask_1(mask: str, bin_num: str) -> int:
    bin_num_list = list(bin_num)
    for ind, num in enumerate(mask):
        if num in ('0', '1'):
            bin_num_list[ind] = num
    return int(''.join(bin_num_list), 2)


total_mem = dict()
for line in raw:
    if 'mask' in line:
        mask = line.split()[-1]
    else:
        addr = re.search(r'\[\d+\]', line).group().strip('[]')
        num = int(line.split()[-1])
        total_mem[addr] = apply_mask_1(mask, get_bin_string(num))

# print(sum(total_mem.values()))


def apply_mask(mask: str, bin_num: str) -> int:
    bin_num_list = list(bin_num)
    for ind, num in enumerate(mask):
        if num in ('1', 'X'):  # make 0 do nothing
            bin_num_list[ind] = num

    possible = combo_str(''.join(bin_num_list))
    decs = [int(p, 2) for p in possible]
    # print(decs)
    return decs


def combo_str(word):
    options = [(c,) if c != 'X' else ('X', '1', '0') for c in word]

    combos = [''.join(o) for o in product(*options)]
    return [i for i in combos if 'X' not in i]


total_mem = dict()
for line in raw:
    if 'mask' in line:
        mask = line.split()[-1]
    else:
        addr = re.search(r'\[\d+\]', line).group().strip('[]')
        num = int(line.split()[-1])

        add_writes = apply_mask(mask, get_bin_string(int(addr)))
        for a in add_writes:
            total_mem[a] = num
print(total_mem)
print(sum(total_mem.values()))
