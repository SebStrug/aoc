from dataclasses import dataclass
from typing import Union, Optional
from math import floor, ceil

RAW_TEST = """[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"""

with open('input_18.txt', 'r') as f:
    RAW = f.read()


@dataclass
class Number:
    parent: Optional['Number']
    l: Union[int, 'Number']
    r: Union[int, 'Number']
    level: int

    @classmethod
    def num_from_list(cls, list_: list):
        top_level = Number(parent=None, l=list_[0], r=list_[1], level=0)
        return Number.unnest_num(top_level.l, top_level.r)

    @classmethod
    def unnest_num(cls, l, r, level:int = 0) -> 'Number':
        if isinstance(l, int):
            left = l
        else:
            left = cls.unnest_num(l=l, level=level+1)
        if isinstance(r, int):
            right = r
        else:
            right = cls.num_from_list(r=r, level=level+1)
        return Number(parent=num, l=left, r=right, level=level)





def list_from_num(n: Number) -> list:
    total = []
    if isinstance(n.l, Number):
        total.append(list_from_num(n.l))
    else:
        total.append(n.l)
    if isinstance(n.r, Number):
        total.append(list_from_num(n.r))
    else:
        total.append(n.r)
    

def split(num: int) -> Number:
    return Number(l=floor(num/2), r=ceil(num/2))

def explode(num: Number, nesting: int) -> Number:
    ...

TEST_1 = [[[[[9,8],1],2],3],4]
TEST_2 = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
num = Number.num_from_list(TEST_2)
