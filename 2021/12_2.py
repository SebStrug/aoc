RAW_TEST = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

RAW_TEST_2 = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

RAW_TEST_3 = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

from collections import defaultdict

with open('input_12.txt', 'r') as f:
    RAW = f.read()

data = tuple(RAW.splitlines())

# dictionary mapping each path to another is key
paths = defaultdict(list)
for p in data:
    p_1, p_2 = p.split('-')
    paths[p_1].append(p_2)
    paths[p_2].append(p_1)

# visited only needs to keep track of lowercase nodes
def path(current: str, visited: set[str], twice: bool):
    if current.islower():
        visited |= {current} 
    
    num_paths = 0
    for n in paths[current]:
        if n == 'end':
            num_paths += 1
        elif n != 'start':
            if n not in visited:
                num_paths += path(n, visited, twice)
            elif not twice:
                num_paths += path(n, visited, True)
    return num_paths

# frozenset is key for immutability
print(path('start', frozenset(), False))
    