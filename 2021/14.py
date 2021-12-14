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

with open('input_14.txt', 'r') as f:
    RAW = f.read()

data = RAW.splitlines()
chain = data[0]
subs = {}
for line in data[2:]:
    k, v = line.split(' -> ')
    subs.update({k: v})

def step(chain: str) -> str:
    new_chain = ''
    for ind in range(len(chain)):
        insert = subs.get(chain[ind:ind+2])
        if insert:
            new_chain += chain[ind]
            new_chain += insert
        else:
            new_chain += chain[ind]
    return new_chain

for _ in range(10):
    chain = step(chain)

from collections import Counter
chain_count = Counter(chain)
# How often the most common character has occurred
most_common = chain_count.most_common(1)[0][1]
least_common_char = min(chain_count, key=chain_count.get)
least_common = sum([1 for c in chain if c == least_common_char])
print(most_common - least_common)