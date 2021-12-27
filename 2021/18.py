import json
from functools import reduce
import itertools
from math import ceil, floor
from typing import Union

RAW_TEST = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""".splitlines()

with open('input_18.txt', 'r') as f:
    RAW = f.read().splitlines()

SnailNumT = Union[int, tuple['SnailNumT', 'SnailNumT']]
data = list(map(json.loads, RAW))

def magnitude(x: SnailNumT) -> int:
    """Recursive solution for magnitude

    Takes in a snail number which is two elements, each of which
    may be a number or a snail number
    """
    if isinstance(x, int):
        return x
    return 3 * magnitude(x[0]) + 2 * magnitude(x[1])


def add_left(x: SnailNumT, n: int):
    """Recursive function used to explode a snail number leftwise
    
    Args:
        x: Snail number
        n: Number to add
    """
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [add_left(x[0], n), x[1]]


def add_right(x, n):
    """Recursive function used to explode a snail number rightwise
    
    Args:
        x: Snail number
        n: Number to add    
    """
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [x[0], add_right(x[1], n)]


def explode(x: SnailNumT, n=4):
    """Explode a number
    
    Args:
        x: Snail number
        n: nesting, keep track of levels, only explode at 4

    Returns:
        - boolean if true
        - resulting left snail number, None if 
        - central value, 0 if at the nesting level
        - resulting right snail number
    """
    if isinstance(x, int):
        return False, None, x, None
    if n == 0:
        return True, x[0], 0, x[1]
    a, b = x
    exp, left, a, right = explode(a, n - 1)
    if exp:
        return True, left, [a, add_left(b, right)], None
    exp, left, b, right = explode(b, n - 1)
    if exp:
        return True, None, [add_right(a, left), b], right
    return False, None, x, None


def split(x: SnailNumT) -> tuple[bool, SnailNumT]:
    """Split a snail number
    
    Returns:
        boolean - true if there was a split
        snail number
    """
    if isinstance(x, int):
        if x >= 10:
            return True, [floor(x/2), ceil(x/2)]
        return False, x
    # recursively split left/right
    a, b = x
    change, a = split(a)
    if change:
        return True, [a, b]
    change, b = split(b)
    return change, [a, b]


def add(a, b):
    x = [a, b]
    # iteratively do explode/split steps until no more changes are made
    while True:
        change, _, x, _ = explode(x)
        if change:
            continue
        change, x = split(x)
        if not change:
            break
    return x

print(magnitude(reduce(add, data)))

from itertools import permutations

print(max(magnitude(reduce(add, perm)) for perm in permutations(data, 2)))