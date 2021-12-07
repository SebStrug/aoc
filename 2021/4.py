RAW_TEST = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

with open('input_4.txt', 'r') as f:
    RAW = f.read()

data = RAW.split('\n')
numbers = [int(n) for n in data[0].split(',')]
boards = []
for line in data[1:-1]:
    if line == '':
        board = []
        boards.append(board)
    else:
        board.append([int(num) for num in line.split()])

import pandas as pd
def check_bingo(df: pd.DataFrame) -> bool:
    for i in range(5):
        if (df.iloc[i] == -1).all():
            return True
        if (df.iloc[:, i] == -1).all():
            return True
    return False

df_boards = [pd.DataFrame(board) for board in boards]
boards_won = {ind: -1 for ind, _ in enumerate(df_boards)}
for n in numbers:
    for ind, df in enumerate(df_boards):
        df[df==n] = -1
        if check_bingo(df):
            sum_unmarked = df[df != -1].sum().sum()
            boards_won[ind] = n * sum_unmarked
        if all(v != -1 for v in boards_won.values()):
            print(n * sum_unmarked)
            raise SystemExit

