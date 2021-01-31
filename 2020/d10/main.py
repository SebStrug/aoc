import itertools as it
from utils import read_files

raw = read_files('d10')
data = set(int(i) for i in raw)

joltage = 0
jolt_1_diffs = 0
jolt_3_diffs = 0
while True:
    print(data, joltage)
    if joltage + 1 in data:
        joltage += 1
        jolt_1_diffs += 1
    elif joltage + 2 in data:
        joltage += 2
    elif joltage + 3 in data:
        joltage += 3
        jolt_3_diffs += 1
    else:
        break
    data.remove(joltage)
joltage += 3
jolt_3_diffs += 1
print(joltage)
print(jolt_1_diffs * jolt_3_diffs)

# part 2
data = sorted(int(i) for i in raw)
iterator = iter(data)
joltage = 0
for i, j in zip(iterator, iterator):
    print(i, j, joltage)
    if j <= i + 3:
        joltage += j - i
print(joltage)


def valid_data(data: set, desired_joltage: int) -> bool:
    joltage = 0
    while True:
        if joltage + 1 in data:
            joltage += 1
        elif joltage + 2 in data:
            joltage += 2
        elif joltage + 3 in data:
            joltage += 3
        else:
            break
        data.remove(joltage)
    return joltage == desired_joltage
