# Just need to solve for y, x is irrelevant for part 1

test = "x=20..30, y=-10..-5"
data_x, data_y = (20, 30), (-10, -5)

data = "x=156..202, y=-110..-69"
data_x, data_y = (156, 202), (-110, -69)

def step_y(y: int, vel_y: int) -> tuple[int, int]:
    return y + vel_y, vel_y -1

max_steps = 1_000

good_ys = []
for vel_y in range(1, 200):
    original_vel_y = vel_y
    y = 0
    for _ in range(max_steps):
        y, vel_y = step_y(y, vel_y)
        if min(data_y) <= y <= max(data_y):
            good_ys.append(original_vel_y)
            break

vel_y = max(good_ys) # 48
y = 0
highest_y = 0
for _ in range(max_steps):
    y, vel_y = step_y(y, vel_y)
    if y > highest_y:
        highest_y = y
    if min(data_y) <= y <= max(data_y):
        break

print(highest_y)
