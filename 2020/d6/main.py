from utils import read_files
from typing import List
from itertools import chain

raw = read_files('d6')

groups = []
temp_group = []
for line in raw:
    if line == '':
        groups.append(temp_group)
        temp_group = []
        continue
    temp_group.append(line)
groups.append(temp_group)


def count_group(group: List[str]) -> int:
    """Count the unique letters in a group"""
    letters = set()
    for person in group:
        letters.update(set(person))
    return len(letters)


group_sum = sum(count_group(g) for g in groups)
print(group_sum)


def count_group_2(group: List[str]) -> int:
    """Count letters which *everyone* in group has"""
    group_sets = [set(g) for g in group]
    return len(set.intersection(*group_sets))


group_sum = sum(count_group_2(g) for g in groups)
print(group_sum)
