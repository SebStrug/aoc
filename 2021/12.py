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

with open("input_12.txt", "r") as f:
    RAW = f.read()

data = tuple(RAW.splitlines())


def get_valid_nodes(current: str, visited: tuple[str], data: list[str]) -> list[str]:
    valid_nodes = []
    for path in data:
        # Can't just filter for current e.g. 'd' is in 'end'
        if f"{current}-" in path or f"-{current}" in path:
            node = path.replace(current, "").replace("-", "")
            if node.isupper() or (node.islower() and node not in visited):
                valid_nodes.append(node)
    return valid_nodes


total = 0


def branch_path(current: str, visited: tuple[str], data: list[str]) -> list[str]:
    global total

    visited = tuple(list(visited) + [current])
    nodes = get_valid_nodes(current, visited, data)
    for n in nodes:
        if n == "end":
            total += 1
        branch_path(n, visited, data)


branch_path("start", tuple(), data)
print(total)
