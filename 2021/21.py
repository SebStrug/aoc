RAW_TEST = """Player 1 starting position: 4
Player 2 starting position: 8"""

RAW = """Player 1 starting position: 8
Player 2 starting position: 10"""

spaces = [8, 10]
scores = [0, 0]
die = 0
rolls = 0


def my_mod(num: int, mod: int) -> int:
    """Modulo to 1 not 0"""
    return (num - 1) % mod + 1


player_ind = 0
while True:
    die += 1
    die = my_mod(die, 100)

    rolls += 1
    spaces[player_ind] += die
    if rolls % 3 == 0:
        spaces[player_ind] = my_mod(spaces[player_ind], 10)

        scores[player_ind] += spaces[player_ind]
        print(f"{spaces=}, {scores=}, {die=}, {rolls=}")
        if any(s >= 1000 for s in scores):
            break
        player_ind = (player_ind + 1) % 2

print(scores[1] * rolls)
