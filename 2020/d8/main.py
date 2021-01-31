from copy import deepcopy
import utils

# raw = utils.read_files('d8', fname='example.txt')
raw = utils.read_files('d8')

init_data = [line.split() for line in raw]
init_data = [[action, int(val)] for action, val in init_data]


def run_accumulator(data) -> int:
    accumulator = 0
    ind = 0
    visited_inds = set()

    while ind not in visited_inds:
        visited_inds.add(ind)
        try:
            action, val = data[ind]
        except IndexError:
            print('Success, reached end')
            return accumulator
        if action == 'acc':
            accumulator += val
            ind += 1
        elif action == 'jmp':
            ind += val
        elif action == 'nop':
            ind += 1
        else:
            raise ValueError
        # print(ind, action, val)
    return -1


print(run_accumulator(init_data))

ind = 0
while True:
    data = deepcopy(init_data)
    if data[ind][0] == 'nop':
        data[ind][0] = 'jmp'
    elif data[ind][0] == 'jmp':
        data[ind][0] = 'nop'
    accum = run_accumulator(data)
    if accum != -1:
        print(accum)
        break
    ind += 1
