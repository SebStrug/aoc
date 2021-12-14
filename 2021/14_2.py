RAW_TEST = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

from collections import defaultdict

with open('input_14.txt', 'r') as f:
    RAW = f.read()

data = RAW.splitlines()
chain_str = data[0]
subs = {}
for line in data[2:]:
    k, v = line.split(' -> ')
    subs.update({k: v})

chain = defaultdict(int)
for ind in range(len(chain_str)):
    chain[chain_str[ind:ind+2]] += 1

def step(chain: dict) -> dict:
    new_chain = defaultdict(int)
    for key in chain.keys():
        sub_val = subs.get(key)
        if sub_val:
            new_chain[key[0]+sub_val] += chain[key]
            new_chain[sub_val+key[1]] += chain[key]
    return new_chain

def unroll_chain(chain: dict) -> dict:
    """Unroll a chain from counts of character couplets to single characters"""
    unrolled = defaultdict(int)
    for couplet in chain.keys():
        unrolled[couplet[0]] += chain[couplet]
        unrolled[couplet[1]] += chain[couplet]
    return unrolled

for _ in range(40):
    chain = step(chain)

unrolled = unroll_chain(chain)
max_val = max(unrolled.values()) / 2
min_val = min(unrolled.values()) / 2

import math
print(math.ceil(max_val - min_val))
