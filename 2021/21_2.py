RAW_TEST = """Player 1 starting position: 4
Player 2 starting position: 8"""

RAW = """Player 1 starting position: 8
Player 2 starting position: 10"""

from functools import lru_cache

spaces = [4, 8]
scores = [0, 0]
die = 0
rolls = 0

def my_mod(num: int, mod: int) -> int:
    """Modulo to 1 not 0"""
    return (num- 1) % mod + 1

@lru_cache()
def play_game(spaces, scores, die, rolls) -> int:
    player_ind = 0
    while True:
        die += 1
        die = my_mod(die, 100)

        rolls += 1
        spaces[player_ind] += die
        if rolls % 3 == 0:
            spaces[player_ind] = my_mod(spaces[player_ind], 10)

            scores[player_ind] += spaces[player_ind]
            print(f'{spaces=}, {scores=}, {die=}, {rolls=}')
            if any(s >= 21 for s in scores):
                # return the ind
                return player_ind
            player_ind = (player_ind + 1) % 2
    
