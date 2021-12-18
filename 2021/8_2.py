RAW_TEST = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

with open("input_8.txt") as f:
    RAW = f.read()

data = RAW.split("\n")

# difficult nums: 5, 2, 3 (length five)
# difficult nums: 9, 6, 0 (length six)

# three has length 5 and has the numbers that one does
# two has length 5 and only has the 1st number from one
# five has length five and only has the 2nd number from one

# nine has all the numbers that three does and is length 6
# six has all the number that five does and is length 6
# zero is the one left over


def contains_num(num: str, contains: str, num_match: int) -> bool:
    return num_match == len(
        list(filter(lambda x: x is True, (char in num for char in contains)))
    )


def solve_line(line) -> int:
    line_map = {}
    digit_strings = [d for d in line.split(" ") if d != "|"]
    for digit_str in digit_strings:
        if len(digit_str) == 2:
            line_map[1] = digit_str
        elif len(digit_str) == 3:
            line_map[7] = digit_str
        elif len(digit_str) == 4:
            line_map[4] = digit_str
        elif len(digit_str) == 7:
            line_map[8] = digit_str

    # while our line map doesn't yet have all the values
    signal, output = line.split("|")
    signal = signal.strip().split(" ")
    while len(signal) != len(line_map.values()):
        for digit in digit_strings:
            if len(digit) == 5:
                if contains_num(digit, line_map[7], 3):
                    line_map[3] = digit
                elif contains_num(digit, line_map[4], 3):
                    line_map[5] = digit
                else:
                    line_map[2] = digit
            elif len(digit) == 6:
                if contains_num(digit, line_map[4], 4):
                    line_map[9] = digit
                elif contains_num(digit, line_map[7], 3):
                    line_map[0] = digit
                else:
                    line_map[6] = digit

    output_str = ""
    for output_ in output.strip().split(" "):
        for k in line_map.keys():
            if len(output_) == len(line_map[k]):
                if contains_num(output_, line_map[k], len(output_)):
                    output_str += str(k)

    return int(output_str)


score = 0
for line in data:
    score += solve_line(line)
print(score)
