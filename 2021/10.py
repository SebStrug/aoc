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

score = 0
for line in data:
    line_ = clean_line_full(line)
    bad_char = get_first_closing(line_)
    if bad_char:
        score += symbol_score[bad_char]
print(score)