# x and y are independent

test = "x=20..30, y=-10..-5"
data_x, data_y = (20, 30), (-10, -5)

data = "x=156..202, y=-110..-69"
data_x, data_y = (156, 202), (-110, -69)

def step_y(y: int, vel_y: int) -> tuple[int, int]:
    return y + vel_y, vel_y - 1

def step_x(x: int, vel_x: int) -> tuple[int, int]:
    x += vel_x
    if vel_x < 0:
        vel_x += 1
    elif vel_x > 0:
        vel_x -= 1
    return x, vel_x        

max_steps = 1_000

valid_x = []
for vel_x in range(300):
    x = 0
    original_vel_x = vel_x
    for _ in range(max_steps):
        x, vel_x = step_x(x, vel_x)
        if min(data_x) <= x <= max(data_x):
            valid_x.append(original_vel_x)
            break

valid_y = []
for vel_y in range(-200, 300):
    y = 0
    original_vel_y = vel_y
    for _ in range(max_steps):
        y, vel_y = step_y(y, vel_y)
        if min(data_y) <= y <= max(data_y):
            valid_y.append(original_vel_y)
            break

import itertools
valid_perms = 0
for vel_x, vel_y in itertools.product(valid_x, valid_y):
    x, y = 0, 0
    for _ in range(max_steps):
        x, vel_x = step_x(x, vel_x)
        y, vel_y = step_y(y, vel_y)
        if (min(data_x) <= x <= max(data_x)) and (min(data_y) <= y <= max(data_y)):
            valid_perms += 1
            break

print(valid_perms)
# 2636 too low!