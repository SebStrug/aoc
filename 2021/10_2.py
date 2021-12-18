from os import supports_bytes_environ
from typing import Optional

RAW_TEST = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

with open("input_10.txt") as f:
    RAW = f.read()

data = RAW.split("\n")

symbol_score = {")": 3, "]": 57, "}": 1197, ">": 25137}
opening_symbols = ("(", "[", "{", "<")
closing_symbols = (")", "]", "}", ">")
open_to_close = dict(zip(opening_symbols, closing_symbols))
close_to_open = dict(zip(closing_symbols, opening_symbols))


def clean_line(line):
    """Clean a line a single time, remove matching opening/closing symbols"""
    new_line = []
    ind = 0
    while ind < len(line):
        char = line[ind]
        prev_char = line[ind - 1]

        if char in opening_symbols:
            new_line.append(char)
            ind += 1
            continue

        # char is a closing symbol
        matching_open_sym = close_to_open.get(char)
        # previous char is matching opening symbol
        if matching_open_sym == prev_char:
            new_line.pop()
            ind += 1
            continue

        new_line.append(char)
        ind += 1
    return "".join(new_line)


def clean_line_full(line):
    """Fully clean a line of matching opening/closing symbols"""
    line_length = len(line)
    while True:
        line = clean_line(line)
        if len(line) == line_length:
            break
        line_length = len(line)
    return line


def get_first_closing(line: str) -> Optional[str]:
    """Get the first closing symbol in a line"""
    for char in line:
        if char in closing_symbols:
            return char
    return None


good_lines = []
for line in data:
    line_ = clean_line_full(line)
    bad_char = get_first_closing(line_)
    if bad_char:
        continue
    good_lines.append(line)

autocomplete_score = {")": 1, "]": 2, "}": 3, ">": 4}


def get_line_score(line: str) -> int:
    line_score = 0
    line_ = clean_line_full(line)
    for char in reversed(line_):
        char_ = open_to_close[char]
        line_score *= 5
        line_score += autocomplete_score[char_]
    return line_score


lines_n_scores = []
for line in good_lines:
    line_n_score_ = (line, get_line_score(line))
    lines_n_scores.append(line_n_score_)
    # print(line_n_score_)

sorted_lns = sorted(lines_n_scores, key=lambda x: x[1])
print(sorted_lns[len(sorted_lns) // 2])
