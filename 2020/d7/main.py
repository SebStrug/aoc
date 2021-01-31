from utils import read_files
import re

raw = read_files('d7', fname='example.txt')

count = 0
descrips = ['shiny gold']
processed_lines = []
while descrips:
    new_descrips = []
    for line in raw:
        if line in processed_lines:
            continue
        init, other = line.split('contain')
        if any(d in other for d in descrips):
            count += 1
            new_descrips.append(init.split('bag')[0].strip())
            processed_lines.append(line)
    descrips = new_descrips
# print(count)


def count_bags(descrip) -> int:
    line = [ln for ln in raw if ln.startswith(descrip)][0]
    print(line)
    other_bags = line.split('bags contain')[1]
    if 'no other' in other_bags:
        return 1
    else:
        descrips = other_bags.split(',')
        descrips = [i.replace('bags', '').replace(
            'bag', '').rstrip('.').strip() for i in descrips]
        nums = [int(re.match(r'\d+', i).group()) for i in descrips]
        descrips = [re.sub(r'\d+', '', i).strip() for i in descrips]
        # print(nums, descrips)
        for i in range(len(nums)):
            print(f'Doing {nums[i]} + {nums[i]} * {descrips[i]}')
        return sum(nums[i] + [(nums[i]*count_bags(descrips[i])) for i in range(len(nums))])
    return -1


descrip = 'shiny gold'
print(count_bags(descrip))
