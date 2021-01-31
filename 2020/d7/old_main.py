import re
from utils import read_files

raw = read_files('d7', fname='example.txt')


def get_descrip(bag):
    num_search = re.match(r'\d+', bag)
    if num_search:
        num = num_search.group()
    else:
        print(bag)
        raise ValueError

    bag_no_num = re.sub(r'\d+', '', bag).strip()
    descrip = re.sub(r'(bag)s?', '', bag_no_num).strip()
    return num, descrip


def process_line(line):
    initial_bag, other_bags = line.split('contain')
    initial_bag = initial_bag.replace('bags', '').strip()
    if 'no other bags' in other_bags:
        return initial_bag, {}

    other_bag_dict = dict()
    for bag in other_bags.split(','):
        num, descrip = get_descrip(bag.strip(' .'))
        other_bag_dict[descrip] = num

    return initial_bag, other_bag_dict


bag_dict = dict()
for line in raw:
    initial_bag, other_bag_dict = process_line(line)
    bag_dict[initial_bag] = other_bag_dict

# 141 too high
good_bags = ['shiny gold']
processed_bags = []
count = 0
while good_bags:
    new_good_bags = []
    for bag in bag_dict:
        if bag in processed_bags:
            continue
        if any(good in bag_dict[bag] for good in good_bags):
            count += 1
            new_good_bags.append(bag)
            processed_bags.append(bag)
    good_bags = new_good_bags
    print(count, good_bags)


processing_bags = ['shiny gold']
count = 1
while processing_bags:
    for bag in processing_bags:
        bags = bag_dict[bag]
