
from typing import Optional, List
from functools import lru_cache
from functools import lru_cache


RAW_TEST = """3,4,3,1,2"""

with open("input_6.txt", "r") as f:
    RAW = f.read()

fishes = [int(num) for num in RAW.split(',')]

@lru_cache(maxsize=None)
def recursive_fish(fish_life: int, days: int) -> int:
    if days == 0:
        return 1

    if fish_life == 0:
        return recursive_fish(6, days - 1) + recursive_fish(8, days - 1)
    else:
        return recursive_fish(fish_life - 1, days - 1)

print(sum(recursive_fish(fish, 256) for fish in fishes))
