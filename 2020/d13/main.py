import itertools as it
from math import gcd
import math
from utils import read_files

raw = read_files('d13')

depart = int(raw[0])
vals = raw[1].split(',')
vals = [int(i) for i in vals if i != 'x']

lowest = 9999999
best_v = None
for v in vals:
    temp = v - (depart % v)
    if temp < lowest:
        lowest = temp
        best_v = v

# print(lowest * best_v)


def find_bus(target_vals, bus: int, bus_ind: int) -> int:
    iterator = it.count(bus, step=bus)
    while True:
        item = next(iterator)
        print(item)
        if int((item - bus_ind) % v) == 0:

            return item


# # lowest common multiple?
# raw = '17,x,13,19'
# target_vals = []
# for ind, v in enumerate(raw.split(',')):
#     if v == 'x':
#         continue
#     if ind == 0:
#         target_vals.append(int(v))

#     print(ind, v)
#     item = find_bus(target_vals, int(v), ind)
#     target_vals.append(item)
#     print()
#     print('ITEM: ', item)

iterator = it.count(19, step=19)
while True:
    item = next(iterator)
    if int((item - 3) % 17) == 0 and int((item-3) % 104) == 0:
        print(item)
        break


def combine_phased_rotations(a_period, a_phase, b_period, b_phase):
    """Combine two phased rotations into a single phased rotation

    Returns: combined_period, combined_phase

    The combined rotation is at its reference point if and only if both a and b
    are at their reference points.
    """
    gcd, s, t = extended_gcd(a_period, b_period)
    phase_difference = a_phase - b_phase
    pd_mult, pd_remainder = divmod(phase_difference, gcd)
    if pd_remainder:
        raise ValueError("Rotation reference points never synchronize.")

    combined_period = a_period // gcd * b_period
    combined_phase = (a_phase - s * pd_mult * a_period) % combined_period
    return combined_period, combined_phase


def arrow_alignment(red_len, green_len, advantage):
    """Where the arrows first align, where green starts shifted by advantage"""
    period, phase = combine_phased_rotations(
        red_len, 0, green_len, -advantage % green_len
    )
    return -phase % period


def extended_gcd(a, b):
    """Extended Greatest Common Divisor Algorithm

    Returns:
        gcd: The greatest common divisor of a and b.
        s, t: Coefficients such that s*a + t*b = gcd

    Reference:
        https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t
