from collections import defaultdict
import re

RAW_TEST = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2"""

with open('input_10.txt', 'r') as f:
    RAW = f.read()

data = RAW.splitlines()

bots = defaultdict(list)
outputs = defaultdict(list)

for line in data:
    if line.startswith('value'):
        value, bot = map(int, re.findall('\d+', line))
        bots[bot].append(value)
        print(line)

def try_lines(data_set: list[str], bots, outputs) ->  tuple[dict, dict]:
    bad_lines = []
    for line in data_set:
        if line.startswith('value'):
            continue
        else:
            bot, low_dest, high_dest = map(int, re.findall('\d+', line))
            if len(bots[bot]) < 2:
                bad_lines.append(line)
                continue
            low_val, high_val = sorted(bots[bot])
            _, low_type, high_type = re.findall('bot|output', line)
            if low_type == 'bot':
                bots[low_dest].append(low_val)
            else:
                outputs[low_dest].append(low_val)
            bots[bot].remove(low_val)
            if high_type == 'bot':
                bots[high_dest].append(high_val)
            else:
                outputs[high_dest].append(high_val)
            bots[bot].remove(high_val)
    return bad_lines, bots, outputs

while len(data) > 0:
    data, bots, outputs = try_lines(data, bots, outputs)
print(outputs[0][0] * outputs[1][0] * outputs[2][0])