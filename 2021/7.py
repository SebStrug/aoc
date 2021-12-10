from functools import lru_cache

RAW_TEST = """16,1,2,0,4,2,7,1,2,14"""

with open("input_7.txt", "r") as f:
    RAW = f.read()

data = list(map(int, RAW.split(",")))


def arithmetic_sequence(a: int, b: int) -> int:
    diff = abs(a - b)
    return diff * (diff + 1) // 2


lowest_num = 0
fuel_to_move = 999_999_999_999
for num in range(min(data), max(data) + 1):
    fuel = sum(arithmetic_sequence(num, x) for x in data)
    if fuel < fuel_to_move:
        fuel_to_move = fuel
        lowest_num = num

print(lowest_num)
print(fuel_to_move)
