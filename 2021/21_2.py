RAW_TEST = """Player 1 starting position: 4
Player 2 starting position: 8"""

RAW = """Player 1 starting position: 8
Player 2 starting position: 10"""

from functools import cache
from collections import Counter
from itertools import product


def my_mod(num: int, mod: int) -> int:
    """Modulo to 1 not 0"""
    return (num - 1) % mod + 1


# Get the distribution of sums of rolling three times (1, 2, or 3)
distrib = Counter(sum(r) for r in product((1, 2, 3), repeat=3))
moves, odds = distrib.keys(), distrib.values()


@cache
def game(pos1: int, pos2: int, score1: int = 0, score2: int = 0) -> tuple[int, int]:
    if score2 >= 21:
        # Add a win to the second player
        return 0, 1

    wins1, wins2 = 0, 0
    for move, odd in zip(moves, odds):
        pos1_ = my_mod(pos1 + move, 10)
        # Swap positions to play the other player's moves
        w2, w1 = game(pos2, pos1_, score2, score1 + pos1_)
        wins1, wins2 = wins1 + (odd * w1), wins2 + (odd * w2)
    return wins1, wins2


print(max(game(8, 10)))
