from utils import read_files
import itertools as it

raw = read_files('d9')
data = [int(i) for i in raw]


def check_vals(num_list):
    return set([sum(i) for i in it.combinations(num_list, 2)])


test_nums = data[:25]
for num in data[25:]:
    if num in check_vals(test_nums):
        test_nums.pop(0)
        test_nums.append(num)
    else:
        # print(num)
        break

# invalid num is 32321523
for ind in range(len(data)):
    accum = it.accumulate(data[ind:])
    count = ind
    while True:
        val = next(accum)
        count += 1
        if val == num:
            print('Success!')
            output_list = data[ind:count]
            print(min(output_list) + max(output_list))
        elif val > num:
            break
