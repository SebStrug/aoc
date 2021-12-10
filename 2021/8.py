from typing import Optional

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


def get_one(line):
    return next(i for i in line if len(i) == 2)

is_one = lambda x: len(x) == 2

def get_four(line):
    return next(i for i in line if len(i) == 4)

is_four = lambda x: len(x) == 4

def get_seven(line):
    return next(i for i in line if len(i) == 3)

is_seven = lambda x: len(x) == 3

def get_eight(line):
    return next(i for i in line if len(i) == 7)

is_eight = lambda x: len(x) == 7

def get_three(line, one: str):
    threes = [i for i in line if len(i) == 5 and all(one_i in i for one_i in one)]
    return threes[0] if len(threes) == 1 else None


def get_two(line, one: str):
    twos = [i for i in line if len(i) == 5 and one[0] in i and one[1] not in i]
    return twos[0] if len(twos) == 1 else None


def get_five(line, one: str):
    return next(i for i in line if len(i) == 5 and one[1] in i and one[0] not in i)


def get_nine(line, three: Optional[str], five: Optional[str]):
    if three:
        nines = [
            i for i in line if len(i) == 6 and all(three_i in i for three_i in three)
        ]
    elif five:
        nines = [i for i in line if len(i) == 6 and all(five_i in i for five_i in five)]
    else:
        return None
    return nines[0] if len(nines) == 1 else None


def get_six(line, five: str):
    sixes = [i for i in line if len(i) == 6 and all(five_i in i for five_i in five)]
    return sixes[0] if len(sixes) == 1 else None


def build_mapping(number_string: str):
    number_list = number_string.split()
    one = get_one(number_list)
    four = get_four(number_list)
    seven = get_seven(number_list)
    eight = get_eight(number_list)
    three = get_three(number_list, one)
    two = get_two(number_list, one)
    five = get_five(number_list, one)
    return {
        one: "1",
        one[::-1]: "1",
        four: "4",
        seven: "7",
        eight: "8",
        three: "3",
        two: "2",
        five: "5",
        get_nine(number_list, three, five): "9",
        get_six(number_list, five): "6",
    }


total = 0
for line in data:
    num_str_only = line.replace("| ", "")
    try:
        mapping = build_mapping(num_str_only)
    except StopIteration:
        print(num_str_only)
        raise

    print(line)
    _, line_outputs = line.split(" | ")
    num = ""
    for num_str in line_outputs.split():
        num += mapping.get(num_str, "0")
    print(num)
    break

# print(total)
